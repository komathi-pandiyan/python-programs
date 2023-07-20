n= 5
arr=[3, 5, 0, 0, 4]
j = 0
for i in range(n):
    if arr[i] != 0:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1
print (arr)