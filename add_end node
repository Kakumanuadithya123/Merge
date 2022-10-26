class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_end(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
                n.ref=new_Node
ll1=linkedlist()
ll1.add_end(10)
ll1.add_end(20)
ll1.add_end(100)
ll1.print_ll()


