def bubble_sort(arr, N):
    for i in range(N):
        for j in range(0, N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
N = 5
arr = [4, 1, 3, 9, 7]
bubble_sort(arr, N)
print("Sorted array:", arr)
