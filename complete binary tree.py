class newNode:
    def __init__ (self,data):
        self.data=data
        self.left=self.right=None
def insertLevelOrder(arr,i,n):
    root=None
    if i<n:
        root=newNode(arr[i])
        root.left=insertLevelOrder(arr,2*i+1,n)
        root.right=insertLevelOrder(arr,2*i+2,n)
    return root
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
arr=[1,2,3,4,5,6,6,6,6]
n=len(arr)
root=None
root=insertLevelOrder(arr,0,n)
inorder(root)
