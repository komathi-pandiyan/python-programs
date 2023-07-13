N=6
a = [ 6, 5, 4, 3, 1, 2 ]
key = 4
first = -1
end = -1
for i in range(N):
    if a[i]==key:
        first = i
for j in range(N-1,-1,-1):
    if a[j] == key:
        end = j
print (end,first)