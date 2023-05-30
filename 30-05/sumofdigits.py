num1=int(input("Enter a starting number"))
num2=int(input("Enter a ending number"))
num1 = num1 - 1
while(num1<num2):
    num1=num1+1
    if(num1%3==0):
        continue
    print(num1)