numbers = [1, 2, 3, 4, 5]
total = 0
count = 0
while count < len(numbers):
    total += numbers[count]
    count += 1
average = total / len(numbers)
print("Average =", average)