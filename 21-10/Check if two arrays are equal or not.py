def are_arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    count_dict1 = {}
    count_dict2 = {}
    for element in arr1:
        count_dict1[element] = count_dict1.get(element, 0) + 1
    for element in arr2:
        count_dict2[element] = count_dict2.get(element, 0) + 1
    return count_dict1 == count_dict2

if __name__ == "__main__":
    A = [1, 2, 5, 4, 0]
    B = [2, 4, 5, 0, 1]
    result = are_arrays_equal(A, B)
    if result:
        print("Output: 1")
    else:
        print("Output: 0")
