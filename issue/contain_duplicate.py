def containsDuplicate(nums) -> bool:
     hashMap={}
     for i in nums :
          print(hashMap)
          if i in hashMap:
               return True
          hashMap[i]= True
     return False
 
def containsDuplicate(nums) -> bool:
     if len(nums)!=len(set(nums)):
          return True
     return False
 
 
 
print(containsDuplicate([1,2,3,1]))  #true
print(containsDuplicate([1,2,3,4])) #false
     