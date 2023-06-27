string1="computer"
string2="cat"
modified_string1 = ""

for char in string1:
    if char not in string2:
        modified_string1 += char
print (modified_string1)

