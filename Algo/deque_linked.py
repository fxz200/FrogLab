from collections import deque

class LinkedDeque:
    def __init__(self):
        self.list = deque()
    
    def add_first(self,e):
        self.list.appendleft(e)
    def add_last(self,e):
        self.list.append(e)
    def remove_first(self):
        self.list.popleft()
    def remove_last(self):
        self.list.pop()
    def peek_first(self):
        return self.list[0]
    def peek_last(self):
        return self.list[-1]
    

if __name__ == "__main__":
    my_deque = LinkedDeque()

    my_deque.add_first(1)
    my_deque.add_first(2)
    my_deque.add_last(3)
    my_deque.add_last(4)

    print(my_deque.remove_first())  # 2
    print(my_deque.remove_last())  # 4
    print(my_deque.peek_first())  # 1
    print(my_deque.peek_last())  # 3