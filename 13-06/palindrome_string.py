n=555
sum=0
total=0
while n!=0:
    sum=n%10
    total=total*10+sum
    n=n//10
if n==total:
	print ("Yes")
else:
	print ("No")