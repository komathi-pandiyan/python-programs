def rearrange_array(arr):
    n = len(arr)
    neg_ptr = 0
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[neg_ptr] = arr[neg_ptr], arr[i]
            neg_ptr += 1
if __name__ == "__main__":
    arr = [-3, 3, -2, 2]
    rearrange_array(arr)
    print("Rearranged array:", arr)