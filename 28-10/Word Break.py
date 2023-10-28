def word_break(A, B):
    n = len(A)
    word_set = set(B)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and A[j:i] in word_set:
                dp[i] = True
                break

    return int(dp[n])
if __name__ == "__main__":
    dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
    input_string = "ilike"
    result = word_break(input_string, dictionary)
    print(result)
