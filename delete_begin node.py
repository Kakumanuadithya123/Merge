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
    def delete_begin(self):
            if self.head is None:
                 print("linkedlist is empty we can't perform deletion")
            else:
                 self.head=self.head.ref

        
ll1=linkedlist()
ll1.delete_begin()
ll1.print_ll()
