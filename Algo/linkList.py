class Node:
    def __init__(self,val):
        self.val= val
        self.next = None
        self.prev = None
        
class LinkList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0
    def get_node(self,index):
        self.check_element_index(index)
        #find first node
        p=self.head.next
        for _ in range(index):
            p=p.next
        return p
    ## check index
    def is_element_index(self,index):
        return 0<= index <self.size
    def check_element_index(self,index):
        if not self.is_element_index:
            raise IndexError(f"Index: {index}, Size: {self.size}")
    def is_position_index(self,index):
        return 0<= index <= self.size
    def check_position_index(self,index):
        if not self.is_position_index:
            raise IndexError(f"Index: {index}, Size: {self.size}")
    ## add
    def add_last(self,e):
        x=Node(e)
        # origin_last <-> x
        origin_last = self.tail.prev
        x.prev=origin_last
        origin_last.next=x
        # origin_last <-> x <-> tail
        x.next=self.tail
        self.tail.prev=x
        self.size+=1
    def add_first(self,e):
        x=Node(e)
        # x <-> origin_first 
        origin_first=self.head.next
        origin_first.prev=x
        x.next=origin_first
        # head <-> x <-> origin_first
        self.head.next=x
        x.prev=self.head
        self.size+=1
    def add(self,index,e):
        self.check_position_index(index)
        if index == self.size:
            self.add_last(e)
            return
        #find origin index node
        origin_index_node=self.get_node(index)
        origin_index_node_pre=origin_index_node.prev
        # origin_pre<-> e <-> origin
        x=Node(e)
        x.prev=origin_index_node_pre
        x.next=origin_index_node
        origin_index_node.prev=x
        origin_index_node_pre.next=x
        self.size+=1
    ##delete
    def remove_first(self):
        if self.size < 1:
            raise IndexError("No elements to remove")
        x = self.head.next
        second = x.next
        # head <-> second
        self.head.next = second
        second.prev = self.head.next
        self.size-=1
        return x.val
    def remove_last(self):
        if self.size < 1:
            raise IndexError("No elements to remove")
        x=self.tail.prev
        x_pre = x.prev
        # x_pre <-> tail
        x_pre.next=self.tail
        self.tail.prev=x_pre
        self.size-=1
        return x.val
    def remove(self,index):
        self.check_element_index(index)
        # find index node
        x = self.get_node(index)
        x_pre = x.pre
        x_next = x.next
        # x_pre <-> x_next
        x_pre.next = x_next
        x_next.pre = x_pre       
        self.size-=1
        return x.val
    ## read
    def get(self,index):
        self.check_element_index(index)
        p=self.get_node(index)
        return p.val
    def get_first(self):
        if self.size < 1:
            raise IndexError("No elements in the list")
        return self.head.next.val
    def get_last(self):
        if self.size < 1:
            raise IndexError("No elements in the list")
        return self.tail.prev.val
    ##update
    def set(self,index,val):
        self.check_element_index(index)
        x=self.get_node(index)
        x.val=val
    
    def size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    
    def display(self):
        print(f"size = {self.size}")
        p = self.head.next
        while p!= self.tail:
            print(f"{p.val} <->",end="")
            p = p.next
        print("null\n")

if __name__ == "__main__":
    list = LinkList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)

    list.display()  