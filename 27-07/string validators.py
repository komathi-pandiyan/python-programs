s ="qA2"
alnum = False
alpha= False
num= False
lower = False
upper = False
for i in s:
    if i.isalpha():
        alpha = True
        alnum = True
    if i.isdigit():
        num= True
        alnum = True
    if i.islower():
        lower= True
    if i.isupper():
        upper = True
print(alnum)
print(alpha)
print(num)
print(lower)
print(upper)