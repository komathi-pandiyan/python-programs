num=(input("enter any string:"))
rev_string=num[::-1]
if num==rev_string:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")