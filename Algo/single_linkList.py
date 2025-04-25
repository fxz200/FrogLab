class SingleLinkList:
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.head
        self.size = 0
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    # Add
    def add_first(self,e):
        new_node = self.Node(e)
        new_node.next=self.head.next
        self.head.next=new_node
        if self.size==0:
            self.tail = new_node
        self.size+=1
    def add_last(self,e):
        new_node = self.Node(e)
        self.tail.next=new_node
        self.tail=new_node
        self.size+=1
    def add(self,index,e):
        self.check_position_index(index)
        if index == self.size:
            self.add_last(e)
            return
        new_node = self.Node(e)
        origin_pre = self.head
        for i in range(index):
            origin_pre=origin_pre.next
        # origin_pre -> new ->origin
        new_node.next=origin_pre.next
        origin_pre.next=new_node
        self.size+=1
    ##delete
    def remove_first(self):
        if self.is_empty():
            raise Exception("NoSuchElementException")
        first=self.head.next
        self.head.next=first.next
        if self.size ==1:
            self.tail = self.head
        self.size-=1
    def remove_last(self):
        if self.is_empty():
            raise Exception("NoSuchElementException")
        last_pre = self.head
        while last_pre.next != self.tail:
            last_pre=last_pre.next
        last_pre.next = None
        self.tail=last_pre
        self.size-=1
    def remove(self,index):
        self.check_element_index(index)
        prev = self.head
        for _ in range(index):
            prev=prev.next
        node_to_remove = prev.next
        prev.next = node_to_remove
        if index == self.size-1:
            self.tail = prev
        self.size-=1
    # read
    def get_first(self):
        if self.is_empty():
            raise Exception("NoSuchElementException")
        return self.head.next.val
    def get_last(self):
        if self.is_empty():
            raise Exception("NoSuchElementException")
        return self.tail.val
    def get(self,index):
        self.check_element_index(index)
        p=self.get_node(index)
        
        return p.val
    def set(self,index,e):
        self.check_element_index(index)
        p = self.get_node(index)
        p.val=e
    ##check index isvalid
    def is_element_index(self,index):
        return 0<=index<self.size
    def is_position_index(self,index):
        return 0<= index<=self.size
    def check_element_index(self,index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
    def check_position_index(self,index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")
    def get_node(self,index):
        #index[0]
        p=self.head.next
        for _ in range(index):
            p=p.next
        return p

if __name__ == "__main__":
    list = SingleLinkList()
    list.add_first(1)
    list.add_first(2)
    list.add_last(3)
    list.add_last(4)
    list.add(2, 5)

    list.remove_first()  # 2
    list.remove_last()   # 4
    list.remove(1)     # 5

    list.set(0,6)
    print(list.get_first())     # 6
    print(list.get_last())      # 3
    print(list.get(1))          # 3