# 給定一個字串 s，請你找出其中不含重複字元的最長子字串的長度。
# Input: "abcabcbb"
# Output: 3
# # 解釋: 最長子字串為 "abc"

# Input: "bbbbb"
# Output: 1
# # 解釋: 最長子字串為 "b"

# Input: "pwwkew"
# Output: 3
# # 解釋: 最長子字串為 "wke"



def length_of_longest_substring(s: str) -> int:
    left=0
    seen=set()
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_len=max(max_len,right-left+1)
            
    return max_len


print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("aaaabcabcbb"))
print(length_of_longest_substring("abcabcbb"))