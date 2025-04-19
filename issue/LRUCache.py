# 請你實作一個 LRU Cache，支援以下兩個操作：
# get(key)：若 key 存在，回傳對應的 value，否則回傳 -1。
# put(key, value)：插入或更新 key 對應的 value。如果超出容量上限，請移除最久沒用過的那個 key。
# 📦 限制：
# cache 容量為固定大小 capacity，由初始化決定。
# 所有操作需在 O(1) 時間內完成（重點考點！）
from collections import OrderedDict
class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.ordered_dict = OrderedDict()
    def put(self,key,value):
        if key in self.ordered_dict:
            del self.ordered_dict[key] ##新增的要在最尾端，所以要刪掉重新加
        elif len(self.ordered_dict)==self.capacity:
            self.ordered_dict.popitem(last=False)
        self.ordered_dict[key]=value    
        return 
    
    def get(self,key):
        try:
            self.ordered_dict.move_to_end(key)
            return(self.ordered_dict[key])
            
        except : return(-1)





cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # 移除 key 2
print(cache.get(2))    # -1
cache.put(4, 4) # 移除 key 1
cache.put(4,5)
print(cache.get(1))    # -1
print(cache.get(3))    # 3
print(cache.get(4))    # 5

