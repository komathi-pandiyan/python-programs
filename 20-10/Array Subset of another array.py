def is_subset(a1, a2):
    set_a1 = set(a1)
    set_a2 = set(a2)
    return set_a2.issubset(set_a1)
if __name__ == "__main__":
    a1 = [11, 7, 1, 13, 21, 3, 7, 3]
    a2 = [11, 3, 7, 1, 7]
    result = is_subset(a1, a2)
    if result:
        print("Yes")
    else:
        print("No")
