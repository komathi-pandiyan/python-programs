def count_occurrences(string, substring):
    count = 0
    start = 0

    while start < len(string):
        index = string.find(substring, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break

    return count

def same_occurrences(str):
    count_cat = count_occurrences(str, 'cat')
    count_hat = count_occurrences(str, 'hat')

    return count_cat == count_hat


input_str = "catinahat"
result = same_occurrences(input_str)
print(result)