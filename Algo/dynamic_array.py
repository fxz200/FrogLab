class DynamicArray:
    INIT_CAP = 1
    def __init__(self,init_capacity=None):
        self.data=[None]*(init_capacity if init_capacity is not None else self.__class__.INIT_CAP)
        self.size = 0
    
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size==0
    #修改容量
    def _resize(self,new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i]=self.data[i]
        self.data=temp
    #確認element index
    def _is_element_index(self,index):
        return 0<= index < self.size
    def _check_element_index(self,index):
        if not self._is_element_index(index):
            raise IndexError(f"Index : {index}, Size : {self.size}")
    #確認element index (for 增)
    def _is_position_index(self,index):
        return 0<= index <= self.size
    def _check_position_index(self,index):
        if not self._is_position_index(index):
            raise IndexError(f"Index : {index} , Size : {self.size}")
    # add
    def add_last(self,e):
        cap = len(self.data)
        #檢查是否需要擴容
        if self.size == cap:
            self._resize(2*cap)
        #尾部插入    
        self.data[self.size]=e
        self.size+=1
    
    def add(self,index,e):
        #check index
        self._check_position_index(index)
        #檢查是否需要擴容
        cap = len(self.data)
        if self.size == cap:
            self._resize(2*cap)
        # data[index..] => data[index+1] 空出位置
        for i in range(self.size-1,index-1,-1):
            self.data[i+1]=self.data[i]
        self.data[index]=e
        self.size +=1
        
    ##性能較差，但無重複代碼    
    def add_last_2(self,e):
        self.add(self.size,e)
        
    def add_first(self,e):
        self.add(0,e)
    
    #delete
    def remove_last(self):
        #array 為空
        if self.size == 0 :
            raise Exception("NoSuchElement")    
        cap = len(self.data)
        #縮容
        if self.size < cap//4:
            self._resize(cap//2)       
        deleted_val = self.data[self.size -1]
        self.data[self.size-1]=None
        self.size-=1
        return deleted_val
    def remove(self,index):
        #check index
        self._check_element_index(index)
        cap = len(self.data)
        #縮容
        if self.size <cap//4:
            self._resize(cap//2)
        deleted_val= self.data[index]
        ## data[index+1..] -> data[index]
        for i in range(index+1,self.size):
            self.data[i-1]=self.data[i]
        self.data[self.size-1]=None
        self.size -=1
        return deleted_val
    def remove_first(self):
        return self.remove(0)
    #update
    def set(self,index,e):
        #check index
        self._check_element_index(index)
        old_val = self.data[index]
        self.data[index]=e
        return old_val        
    #read
    def get(self,index):
        self._check_element_index(index)
        return self.data[index]

if __name__ =="__main__":
    arr = DynamicArray(init_capacity=3)
    arr.add(0,1)
    for i in range(5):
        arr.add_last(9)
    print(arr.remove(0))
    print(arr.set(2,7))

    print(arr.get(0),arr.get(1),arr.get(2))