s="Geeks5"
s1 = ""
s2 = ""
for i in s:
    if i.isalpha():
        s2 = s2 + i 
    elif i.isdigit():
        s1 = s1+i
if len(s2)== int(s1):
    print (1)
else:
    print (0)