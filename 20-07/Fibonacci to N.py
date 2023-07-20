N=1
x=[0,1]
a=0
while a<=N:
    a=x[-1]+x[-2]
    if a>N:
        break
    x.append(a)
print (x)