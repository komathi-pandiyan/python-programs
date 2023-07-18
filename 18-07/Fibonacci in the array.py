N = 9
arr=[4, 2, 8, 5, 20, 1,40, 13, 23]
val = []
n1 = 0
n2 = 1
for i in range(1000):
    val.append(n1)
    res = n1+n2
    n1=n2
    n2=res
        
count= 0
for i in arr:
    if i in val:
        count+=1
        
print (count)
