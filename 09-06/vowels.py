num=input("enter the string")
ind=0
count=0
l=len(num)
while ind<l:
    if num[ind]=='a' or num[ind]=='e' or num[ind]=='i' or num[ind]=='o' or num[ind]=='u':
        count=count+1
    ind=ind+1
print(count)    