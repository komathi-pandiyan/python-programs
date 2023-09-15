binary_str = input("Enter a binary number: ")
decimal_num = 0
for digit in binary_str[::-1]:
    decimal_num += int(digit) * (2 ** (len(binary_str) - 1 - binary_str.index(digit)))
octal_num = ""
while decimal_num > 0:
    remainder = decimal_num % 8
    octal_num = str(remainder) + octal_num
    decimal_num //= 8
print(f"The octal equivalent of {binary_str} is {octal_num}")
