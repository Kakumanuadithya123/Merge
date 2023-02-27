def linear_search(array,k,x):
    for i in range(0,k):
        if(array[i]==x):
            return i
    return -1

array=[]
k=int(input("enter size of array:"))
for i in range(k):
   array.append(input("element in the array[{}]:".format(i)))
print(array)
x=input("enter the element to be searched:")
result=linear_search(array,k,x)
if result==1:
    print("element not there:")
else:
    print("element is there at",result+1)
