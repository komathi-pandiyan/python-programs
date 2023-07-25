n = 5
arr=[1,2,3,4,5] 
k = 4
ind=0
found=False
while ind<k:
    if arr[ind]==k:
        found=True
        print(ind)
        break
    ind=ind+1
if found==False:
    print (-1)
    