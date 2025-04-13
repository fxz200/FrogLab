# 請你實作一個函數 is_valid(s: str) -> bool，來判斷一個只包含以下三種括號的字串是否是「有效的括號匹配」。
# 字元只會是：(){}[]

# Input: "([{}])"
# Output: True

# Input: "([)]"
# Output: False


def is_valid(s:str)->bool:
    stack=[]
    for i in s:
        if i=="(" or i=="[" or i=="{": 
            stack.append(i)
        else:
            if i==")":i="("
            if i=="]":i="["
            if i=="}":i="{"
            if not stack or i!=stack[-1] : return False
            else:
                stack.pop()
           
    if len(stack)!=0:return False
    return True



def is_valid(s:str)->bool:
    stack=[]
    match = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
    for i in s:
        if i in "({[": 
            stack.append(i)
        else:
            if not stack or stack[-1]!=match[i]:
                return False
            stack.pop()
    return len(stack)==0
    
    
print(is_valid("([{}])"))    
print(is_valid("([)]"))   
print(is_valid("]"))   
print(is_valid("((("))   