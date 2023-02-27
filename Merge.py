def MergeSort(a,l,h):
    b=[]
    l=0
    h=len(a)
    if l<h:
        mid=(l+h)//2
        MergeSort(a,l,mid)
        MergeSort(a,mid+1,h)
        Merge(a,l,mid,h)
def Merge(a,l,mid,h):
    i=1
    j=mid+1
    k=0
    while i<=mid and j<=h:
        if a[i]<=a[j]:
            b[k]=a[i]
            i=i+1
        else:
            b[k]=a[j]
            j=j+1
        k=k+1
    while i<=mid:
        b[k]=a[i]
        i=+1
        k=k+1
    while j<=h:
        b[k]=a[j]
        j=j+1
        k=k+1
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
l=0
h=len(a)
MergeSort(a,l,h)
