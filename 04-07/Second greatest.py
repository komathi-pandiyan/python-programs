arr= [10, 5, 10]
arr=list(set(arr))
if(len(arr)>1):
    arr.sort()
    print (arr[-2])
else:
    print (-1)