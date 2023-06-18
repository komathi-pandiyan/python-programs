num = int(input("Enter a number: "))
original = num
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10
if original == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
