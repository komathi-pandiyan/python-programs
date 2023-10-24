def find_triplet_sum(arr, X):
    n = len(arr)
    arr.sort()

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == X:
                return 1

            elif current_sum < X:
                left += 1

            else:
                right -= 1

    return 0
if __name__ == "__main__":
    n = 6
    X = 13
    arr = [1, 4, 45, 6, 10, 8]
    result = find_triplet_sum(arr, X)
    print(result)

