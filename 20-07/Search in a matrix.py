N = 3
M = 3
mat=([3,30,38],
    [44,52,54],
    [57,60,69])
X = 62
r,c = 0,M-1
        
while(r<N and c>=0):
    if mat[r][c]==X:
        print (1)
    elif mat[r][c]<X:
        r+=1
    else:
        c-=1
                
print (0)