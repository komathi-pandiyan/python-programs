#Write a program that prompts the user to enter a positive integer and calculates its factorial using a while loop.
num=int(input("Enter a positive integer:"))

fact = 1
i = 1
while(i<=num):
    fact=fact*i 
    i=i+1
    print(fact)
