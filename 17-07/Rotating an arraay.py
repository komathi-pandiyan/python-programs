n= 7
arr= [1, 2, 3, 4, 5, 6, 7]
d= 2
temp=[]
for i in range(0,d): 
    temp.append(arr[i])
for i in range(d,n):
    arr[i-d]=arr[i]
for i in range(n-d,n): 
    arr[i]=temp[i-(n-d)] 
print (arr)