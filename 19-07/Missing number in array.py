n=5
array=[1,2,3,5]
array.sort()
array.append("a")
for i in range(1,n+1):
    if i!=array[i-1]:
        print (i)
        break