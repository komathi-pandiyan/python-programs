#Write a program that prompts the user to enter a number. Determine whether the number is positive, negative, or zero 
#and display an appropriate message.
num=int(input("Enter a number"))
if(num>=1):
    print(num,"is positive")
elif(num<=-1):
    print(num,"is a negative")
else:
    print("zero")
