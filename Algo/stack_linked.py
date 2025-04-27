from collections import deque
##用deque來模擬double Linked List
#將linked list 尾部作為 stack top
class LinkedStack:
    def __init__(self):
        self.list = deque()
    
    def push(self,e):
        self.list.append(e)
    def pop(self):
        self.list.pop()
    def peek(self):
        return self.list[-1]
    def size(self):
        return len(self.list)
    
    
if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
        
        
    

