def search(list,low,high):
    low=0
    high=n-1
    while(low<=high):
        mid=low+(high-low)//2
        if(list[mid]==key):
           return mid
        else:
            if(list[mid]<key):
              low=mid+1
            else:
              high=mid-1
    return -1
list=[]
n=int(input("enter the no. of elements"))
for i in range (0,n):
    element=int(input())
    list.append(element)
key=int(input("enter the number for searching"))
result=search(list,n,key)
if(result==-1):
    print("key not found")
else:
    print("key found")
 
