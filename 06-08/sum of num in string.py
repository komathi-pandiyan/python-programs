s = "14a4bc23"
sum = 0
current_number = ""
for char in s:
    if char.isdigit():
        current_number += char
    elif current_number:
        sum += int(current_number)
        current_number = ""
if current_number:
    sum += int(current_number)
print(sum)
