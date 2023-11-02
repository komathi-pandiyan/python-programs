def equilibrium_point(arr, n):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(n):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i + 1 
        left_sum += arr[i]
    return -1 
n = 5
arr = [1, 3, 5, 2, 2]
result = equilibrium_point(arr, n)
print(result)
