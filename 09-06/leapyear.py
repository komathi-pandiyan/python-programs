num1=int(input("enter any year"))
if num1%400==0and num1%100==0:
    print(num1,"is a leap year")
else:
    print(num1,"is not a leap year")