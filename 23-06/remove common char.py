def modify_strings(s1, s2):
    result = ''
    for char in s1:
        if char not in s2:
            result += char
    
    for char in s2:
        if char not in s1:
            result += char
    
    if result == '':
        result = -1
    
    return result


s1 = "aacdb"
s2 = "gafd"
result = modify_strings(s1, s2)
print(result)
