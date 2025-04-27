#用array 尾部當stack top => O(1)
#若用頭部會是O(n)，需要用CycleArray才會是O(1)

class ArrayStack:
    def __init__(self):
        self.list=[]
    def push(self,e):
        self.list.append(e)
    def pop(self):
        self.list.pop()
    def peek(self):
        return self.list[-1]
    def size(self):
        return len(self.list)

if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.peek())
    print(stack.size())