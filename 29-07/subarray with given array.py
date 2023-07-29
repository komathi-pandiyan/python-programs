n= 5
s = 12
arr=[1,2,3,7,5]
l = 0
sum = 0
if arr[l] == s:
    print ([1,1])
            
if s == 0:
    print ([-1])
for r in range(n):
    sum = sum + arr[r]
    while sum > s:
        sum -= arr[l]
        l = l + 1
        if sum == s:
            print ([l+1, r+1])

print ([-1])