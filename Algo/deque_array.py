##需要用環形數組來確保從頭刪除或加入是 O(1)
from circular_array import CycleArray
class ArrayQueue:
    def __init__(self):
        self.arr=CycleArray()
    
    def add_last(self,e):
        self.arr.add_last(e)
    def add_first(self,e):
        self.arr.add_first(e)
    def remove_last(self):
        self.arr.remove_last()
    def remove_first(self):
        self.arr.remove_first()
    def peek_first(self):
        return self.arr.get_first()
    def peek_last(self):
        return self.arr.get_last()
    

if __name__ == "__main__":
    my_deque = ArrayQueue()
    my_deque.add_first(1)
    my_deque.add_first(2)
    my_deque.add_last(3)
    my_deque.add_last(4)

    print(my_deque.remove_first())  # 2
    print(my_deque.remove_last())  # 4
    print(my_deque.peek_first())  # 1
    print(my_deque.peek_last())  # 3