s=input()
n=int(input())
sum=0
for i in s:
    sum+=int(i)
sum*=n
s=str(sum)
while len(s)>1:
    sum=0
    for i in s:
        sum+=int(i)
    s=str(sum)

print(s)