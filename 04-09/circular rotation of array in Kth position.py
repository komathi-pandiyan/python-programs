def rotateArray(arr, n, d):
    
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
    
arr = [1, 2, 3, 4, 5]
n = len(arr)
d = 2
result = rotateArray(arr, n, d)


    
print(result)      