#Write a program that prompts the user to enter a positive integer and calculates the sum of its digits using a while loop.
num=int(input("Enter a positive integeer"))
tot=0
while(num>0):
    dig=num%10
    tot=tot+dig
    num=num//10
print("The total sum of digits is:",tot)