# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
def twoSum(nums,target):
    for i in range(len(nums)):
        if target-nums[i] in nums and nums.index(target-nums[i])!=i :
            return [nums.index(target-nums[i]),i]

def twoSum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        if target-nums[i] in hashmap:
            return [hashmap[target - nums[i]], i]
        else :  hashmap[nums[i]] = i



print(twoSum([3,2,4],6))
print(twoSum([2,2,4],4))