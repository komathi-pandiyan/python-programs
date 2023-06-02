num1=int(input("enter any numbers:"))
num2=int(input("enter any numbers:"))
num3=int(input("enter any numbers:"))
if(num1<num2 and num1<num3):
    print(num1,"is a smallest")
elif(num2<num1 and num2<num3):
    print(num2,"is a smallest")    
else:
    print(num3,"is a smallest")