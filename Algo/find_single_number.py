# 給定一個整數陣列，除了某個元素只出現一次外，其餘元素都出現兩次，請找出這個只出現一次的元素。
# Input: [4, 1, 2, 1, 2]
# Output: 4

from typing import List

def find_single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
#0^1=1
#1^2=3
#3^1=2
#2^4=6
#6^2=4
# 4 沒被消除掉

print(3^3^2^1^1)
# a ^ a = 0
# a ^ 0 = a

print(find_single_number([ 1, 2, 1, 4,2]))