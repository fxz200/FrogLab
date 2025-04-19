# 請實作一個函數 compress_string(s: str) -> str，將字串中的連續重複字元進行壓縮，例如：

# 輸入："aaabbccccd"
# 輸出："a3b2c4d1"
# 壓縮的方式是：將連續重複的字元，轉為「字元+重複次數」的格式。

# 不需要考慮原字串長度與壓縮結果的比較（即使壓縮後更長也沒關係）。


def compress_string(s:str):
    textList=[]
    time=[]
    pre=""
    for i in range(len(s)):
        if s[i]!=pre:
            textList.append(s[i])
            time.append(i)    
        pre=s[i]
    time.append(len(s))    
    result=""
    for i in range (len(textList)):
        result=result+textList[i]+str(time[i+1]-time[i])
    return result

def compress_string_ans(s:str):
    result=""
    count=1
    for i in range(1,len(s)):
        if (s[i]==s[i-1]):
            count+=1
        else:
            result+=s[i-1]+str(count)
            count=1
    result+=s[i-1]+str(count)
    return result

print(compress_string_ans("aaabbccccdd")) ##"a3b2c4d1"