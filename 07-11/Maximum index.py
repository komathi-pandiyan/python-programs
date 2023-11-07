def max_index_difference(N, arr):
    if N < 2:
        return 0
    left_min_index = [0] * N
    left_min_index[0] = 0
    for i in range(1, N):
        if arr[i] < arr[left_min_index[i - 1]]:
            left_min_index[i] = i
        else:
            left_min_index[i] = left_min_index[i - 1]
    max_difference = -1
    for j in range(N - 1, 0, -1):
        while j > 0 and arr[left_min_index[j - 1]] < arr[j]:
            max_difference = max(max_difference, j - left_min_index[j - 1])
            j -= 1
    return max_difference
N = 2
arr = [1,10]
result = max_index_difference(N, arr)
print(result)
