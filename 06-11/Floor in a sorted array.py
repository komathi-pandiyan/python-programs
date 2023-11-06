def find_floor(arr, N, x):
    low, high = 0, N - 1
    floor_index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            floor_index = mid
            low = mid + 1
        else:
            high = mid - 1

    return floor_index
N = 7
x = 0
arr = [1, 2, 8, 10, 11, 12, 19]

result = find_floor(arr, N, x)

print(result)
