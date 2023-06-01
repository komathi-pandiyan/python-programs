num=int(input("Enter any num"))
count=0
while num!=0:
    digits=num%10
    count=count*10+digits
    num=num//10
print("The reverse num is",count)    