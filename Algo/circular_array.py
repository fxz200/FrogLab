##左閉右開
class CycleArray:
    def __init__(self,size=1):
        self.size = size
        self.arr=[None]*size
        self.start = 0 #閉區間(包含)，指向第一個有效元素的位置
        self.end =0 #開區間(不包含)，指向最後一個有效元素的下一個位置
        self.count =0
    
    #擴縮容
    def resize(self,newSize):
        new_arr = [None] *newSize
        #複製舊arr元素 => 新arr
        for i in range(self.count):
            ##從start開始
            new_arr[i]=self.arr[(self.start+i)%self.size]
        self.arr=new_arr
        #重置指針
        self.start=0
        self.end= self.count
        self.size=newSize
    def is_full(self):
        return self.size == self.count
    def size(self):
        return self.count
    def is_empty(self):
        return self.count==0
    
    def add_first(self,val):
        if self.is_full():
            self.resize(self.size*2)
        # + self.size 先加一圈再取模 
        self.start=(self.start-1 + self.size )%self.size
        self.arr[self.start]=val
        self.count+=1
    def remove_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        self.arr[self.start]=None
        self.start=(self.start+1)%self.size
        self.count-=1
        if self.count > 0 and self.count <= self.size //4 :
            self.resize(self.size//2)
    def add_last(self,val):
        if self.is_full():
            self.resize(self.size*2)
        self.arr[self.end] = val
        self.end = (self.end+1)%self.size
        self.count+=1
    def remove_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        self.end = (self.end-1+self.size)%self.size
        self.arr[self.end]=None
        self.count-=1
        if self.count > 0 and self.count <= self.size // 4:
            self.resize(self.size //2)
    def get_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[self.start]
    def get_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[(self.end-1+self.size)%self.size]
    
    
arr = CycleArray(6)
arr.add_last(1)
arr.add_last(2)
#[1, 2, _, _, _, _]

arr.add_first(3)
#[1, 2, _, _, _, 3]

arr.add_first(4)
#[1, 2, _, _, 4, 3]

first = arr.get_first() #4
last = arr.get_last() #2
print(first)
print(last)
arr.add_first(5)
#[1, 2, _, 5, 4, 3]

arr.remove_last()
#[1, _, _, 5, 4, 3]

arr.remove_first()
#[1, _, _, _, 4, 3]

arr.remove_last()
#[_, _, _, _, 4, 3]

arr.remove_last()
#[_, _, _, _, 4, _]