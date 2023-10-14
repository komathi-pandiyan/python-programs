def rotate_array_by_one(arr):
    if not arr:
        return arr

    n = len(arr)
    last_element = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_element


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    rotate_array_by_one(arr)

    print("Array after rotation:", arr)
