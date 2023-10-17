def find_element_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    x = 3
    result = find_element_index(arr, x)
    print(result)
