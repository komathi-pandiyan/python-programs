def print_numbers(n):
    if n < 0:
        for i in range(n, 1):
            print(i, end=' ')
        print(0)
    elif n > 0:
        for i in range(n-1, -1, -1):
            print(i, end=' ')
        print(0)
    else:
        print(0)
number = int(input("Enter a number: "))
print_numbers(number)
