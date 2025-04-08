package main

import (
	"context"
	"fmt"
	"net/http"

	"encoding/json"

	"github.com/go-redis/redis/v8"
	"github.com/golang-jwt/jwt"

	"os"
	"time"

	"github.com/gorilla/mux"

	"github.com/google/uuid"

	"github.com/joho/godotenv"
)

var (
	jwtSecretKey           []byte
	rdb                    *redis.Client
	accessTokenExpiration  = 15 * time.Minute
	refreshTokenExpiration = 7 * 24 * time.Hour
)

func init() {
	// Load .env file
	err := godotenv.Load()
	if err != nil {
		fmt.Println("Error loading .env file")
	}
	jwtSecretKey = []byte(os.Getenv("JWT_SECRET_KEY"))
}

type User struct {
	ID   string `json:"id"`
	Name string `json:"name"`
}
type TokenDetails struct {
	AccessToken  string `json:"access_token"`
	RefreshToken string `json:"refresh_token"`
}

var ctx = context.Background()

func storeRefreshToken(UserId, refreshToken string) error {
	err := rdb.Set(ctx, refreshToken, UserId, refreshTokenExpiration).Err()
	if err != nil {
		return err
	}
	return nil
}
func createTokens(user User) (*TokenDetails, error) {
	accessToekn := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"user_id": user.ID,
		"exp":     time.Now().Add(accessTokenExpiration).Unix(),
	})
	accessToeknString, err := accessToekn.SignedString(jwtSecretKey)
	if err != nil {
		return nil, fmt.Errorf("failed to sign access token: %v", err)
	}
	refreshToken := uuid.New().String()
	err = storeRefreshToken(user.ID, refreshToken)
	if err != nil {
		return nil, fmt.Errorf("failed to store refresh token: %v", err)
	}
	return &TokenDetails{
		AccessToken:  accessToeknString,
		RefreshToken: refreshToken,
	}, nil

}

func refreshTokenHandler(w http.ResponseWriter, r *http.Request) {
	var request struct {
		RefreshToken string `json:"refresh_token"`
	}
	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}

	UserID, err := rdb.Get(ctx, request.RefreshToken).Result()
	if err == redis.Nil {
		http.Error(w, "login again", http.StatusUnauthorized)
		return
	} else if err != nil {
		http.Error(w, "Internal server error", http.StatusInternalServerError)
		return
	}

	user := User{ID: UserID}
	accessToken := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"user_id": user.ID,
		"exp":     time.Now().Add(accessTokenExpiration).Unix(),
	})
	accessTokenString, err := accessToken.SignedString(jwtSecretKey)
	if err != nil {
		http.Error(w, "Could not generate new access token", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{
		"access_token":  accessTokenString,
		"refresh_token": request.RefreshToken, // return refreshToken
	})
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	// test data
	user := User{
		ID:   "1234",
		Name: "John Doe",
	}

	tokens, err := createTokens(user)
	if err != nil {
		http.Error(w, fmt.Sprintf("Could not create tokens: %v", err), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(tokens)
}
func keyFunc(token *jwt.Token) (interface{}, error) {
	if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
		return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
	}
	return jwtSecretKey, nil
}
func validateTokenHandler(w http.ResponseWriter, r *http.Request) {
	tokenString := r.Header.Get("Authorization")
	if tokenString == "" {
		http.Error(w, "Missing access token", http.StatusUnauthorized)
		return
	}

	token, err := jwt.Parse(tokenString, keyFunc)
	fmt.Println("token:", token)
	if err != nil || !token.Valid {
		http.Error(w, "Invalid or expired access token", http.StatusUnauthorized)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{
		"message": "Access token is valid",
	})
}
func main() {
	fmt.Println("JWT_SECRET_KEY:", jwtSecretKey)
	// Initialize Redis client
	rdb = redis.NewClient(&redis.Options{
		Addr:     "localhost:6379", // Redis server address
		Password: "",               // No password set
		DB:       0,                // Use default DB
	})

	// Test Redis connection
	pong, err := rdb.Ping(ctx).Result()
	if err != nil {
		fmt.Println("Failed to connect to Redis:", err)
	} else {
		fmt.Println("Redis connected:", pong)
	}

	r := mux.NewRouter()
	r.HandleFunc("/login", loginHandler).Methods("POST")
	r.HandleFunc("/refresh-token", refreshTokenHandler).Methods("POST")
	r.HandleFunc("/validate-token", validateTokenHandler).Methods("GET")
	http.ListenAndServe(":8080", r)
}
