#Write a program that prompts the user to enter a numeric grade. 
#Convert the grade to a letter grade according to the following scale: 90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F.
num=float(input("Enter a numeric grade from 60-100""="))
if(num>=90):
    print("The grade is: A")
elif(num>=80):
    print("The grade is: B")
elif(num>=70):
    print("The grade is: C")
elif(num>=60):
    print("The grade is: D")  
else:
    print("The grade is: F (below 60)")
