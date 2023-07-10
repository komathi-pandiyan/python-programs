n= 8
k= 3
arr=[1, 2, 3, 4, 5, 6, 7, 8]
for i in range(n):
    if i == k-1:
       first  = arr[k-1]
       second = arr[-k]
       arr[-k] = first
       arr[k-1] = second
print (arr)
    