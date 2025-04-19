# 設計一個函式來判斷一個數字是否為「回文數字」。
# 回文數字是指正著讀和反著讀都一樣的數字，例如 121 或 12321。

# 要求：

# 不允許將數字轉換成字串來處理。

# 請寫出一個時間複雜度為 O(log n) 的解法。


def is_palindrome_number(num) :
    numList=[]
    while num>=1:
        numList.append(num%10)
        num=num//10
    for i in range(len(numList)//2):
        if (numList[i]!=numList[-(i+1)]):
            return False
    return True

def is_palindrome_number_ans(n):
    if n < 0 or (n % 10 == 0 and n != 0):
        return False
    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n = n // 10
    print(n,reversed_half)
    return n == reversed_half or n == reversed_half // 10


print(is_palindrome_number_ans(12321))  # True