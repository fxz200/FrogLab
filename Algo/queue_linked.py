from collections import deque

class LinkedQueue:
    def __init__(self):
        self.list = deque()
    def push(self,e):
        self.list.append(e)
    def pop(self):
        self.list.popleft()
    def peek(self):
        return self.list[0]
    def size(self):
        return len(self.list)
        
        


if __name__ == "__main__":
    queue = LinkedQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek()) # 1
    print(queue.pop()) # 1
    print(queue.pop()) # 2
    print(queue.peek()) # 3