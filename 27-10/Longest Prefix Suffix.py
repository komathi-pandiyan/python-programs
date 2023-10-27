def longest_prefix_suffix(s):
    n = len(s)
    lps = [0] * n
    j = 0
    i = 1

    while i < n:
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    return lps[-1]
if __name__ == "__main__":
    input_string = "abab"
    result = longest_prefix_suffix(input_string)
    print("Length of the longest proper prefix which is also a proper suffix:", result)
