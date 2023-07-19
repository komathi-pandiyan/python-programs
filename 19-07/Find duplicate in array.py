N = 5
arr=[0,2,3,1,2]
arr.sort()
d=["_"]
s=["_"]
for i in range(len(arr)):
    if arr[i] != s[-1]:
        s.append(arr[i])
    else:
        if arr[i]!=d[-1]:
            d.append(arr[i])
if d==["_"]:
    print (-1)
else:
    print (d[1::])