num=int(input("enter the num"))
i=2
n=0
while i<num:
    if num%i==0:
        n=1
        print(num,"is not a prime")
    i=i+1
if n==0:
    print(num,"is a prime")