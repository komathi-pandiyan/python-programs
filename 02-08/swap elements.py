n=10
k=5
arr=[1,2,3,5,4,6,7,8,9,10]
for i in range(n):
    if i==k-1:
        first=arr[k-1]
        second=arr[-k]
        arr[-k]=first
        arr[k-1]=second
print(arr)        