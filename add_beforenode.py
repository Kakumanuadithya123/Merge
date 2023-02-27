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
    def add_after (self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in ll")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
ll1=linkedlist()
ll1.add_after(100,30)
ll1.print_ll()
