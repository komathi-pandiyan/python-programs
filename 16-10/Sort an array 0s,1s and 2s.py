def sort012(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
if __name__ == "__main__":
    arr = [0, 2, 1, 2, 0]
    print("Original array:", arr)
    sort012(arr)
    print("Sorted array:", arr)
