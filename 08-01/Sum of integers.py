string= input('Enter a string: ')
sum=0
for i in string:
    if i.isdigit():
        sum=sum+int(i)
print("sum=",sum)