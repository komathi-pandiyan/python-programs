def subarray_sum(arr, n, target_sum):
    current_sum = arr[0]
    start = 0

    for end in range(1, n + 1):
        while current_sum > target_sum and start < end - 1:
            current_sum -= arr[start]
            start += 1

        if current_sum == target_sum:
            return [start + 1, end]  

        if end < n:
            current_sum += arr[end]

    return [-1]  
N = 5
S = 12
A = [1, 2, 3, 7, 5]

result = subarray_sum(A, N, S)
print(result)
