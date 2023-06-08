import random
r = random.randint(1,100)
print(r)
n=int(input("enter number"))
if r<n:
    print("The num is too low.")
elif r>n:
    print("The num is too high.")
else:
    print("equal")
