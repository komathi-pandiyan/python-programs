import math
n=6
s = 1
a = int(math.sqrt(n))
for i in range(2, a+1):
    if n%i==0:
        if i*i==n:
            s = s + i
        else:
            b = n//i
            s = s + i+ b
print (s)