def convert_to_wave(arr):
    n = len(arr)
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    convert_to_wave(arr)
    print("Wave-like array:", arr)
