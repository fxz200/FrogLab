##由於queue一定要從array頭部刪除或加入 => O(N)
#所以需要用環形數組
from circular_array import CycleArray

class ArrayQueue:
    def __init__(self):
        self.list=CycleArray()
    def push(self,e):
        self.list.add_last(e)
    def pop(self):
        self.list.remove_first()
    def peek(self):
        return self.list.get_first()
    def size(self):
        return self.list.size()
    







if __name__ == "__main__":
    queue = ArrayQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(queue.peek()) # 1
    print(queue.pop()) # 1
    print(queue.pop()) # 2
    print(queue.peek()) # 3