N=5
Arr=[1,2,3,4,5]
odd = 0
even = 0
for i in range(N):
    if i % 2 == 0:
        even += Arr[i]
    else:
        odd += Arr[i]
print (even,odd)