table_number =int(input())
sum = 0
for i in range(1, 11):
    value = table_number * i
    print(value, end=" ")
    sum = sum + value
print()
print(sum)