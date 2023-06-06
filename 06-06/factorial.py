num=int(input("Enter the number"))
i=1 
total=1
while i<=num:
    sum=num*i
    total=total*sum
    num=num-1
print("factorial",total)     