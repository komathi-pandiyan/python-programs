num=int(input("Enter any num"))
total=0
while num>0:
    digits=num%10
    total=total+digits
    num=num//10
print("The sum of digits is",total)
 