n=input("enter any string:")
count=0
ind=0
l=len(n)
while ind<l:
    if(n[ind]=='a' or n[ind]=='e' or n[ind]=='i' or n[ind]=='o' or n[ind]=='u'):
        count=count+1 
    ind=ind+1    
print(count)    
