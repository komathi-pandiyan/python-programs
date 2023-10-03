def Calculate(m, n):
    sum = 0
    for i in range(m, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            sum = sum + i
    return sum


m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
result = Calculate(m, n)
print(result)
