n=int(input("How many terms"))
n1,n2=0,1
count=0
if n<=0:
    print("pls enter positive integer")
elif n==1:
    print ("Fibonacci sequencce upto",n,":")
    print(n1)
else:
    print("Fibonacci Sequence:")
    while count<n:
     print(n1)
     nth=n1+n2
     n1=n2
     n2=nth
     count=count+1    