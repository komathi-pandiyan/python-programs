string="Hello World"
vowels = ['a', 'e', 'i', 'o', 'u']
string = list(string)  
left = 0
right = len(string) - 1

while left < right:
    if string[left] in vowels and string[right] in vowels:
            
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    elif string[left] in vowels:
        right -= 1
    else:
            
        left += 1
print(''.join(string))