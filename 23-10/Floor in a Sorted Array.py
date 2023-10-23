def find_floor_index(arr, x):
    n = len(arr)
    low, high = 0, n - 1
    floor_index = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            floor_index = mid
            low = mid + 1

        else:
            high = mid - 1

    return floor_index
if __name__ == "__main__":
    arr = [1, 2, 8, 10, 11, 12, 19]
    x = 0
    result = find_floor_index(arr, x)
    print("Output:", result)
