n = 7
x = 6
arr=[1, 2, 8, 10, 11, 12, 19] 
smaller,larger = 0,0
for i in arr:
    if i <= x:
        smaller += 1
                
    if i >= x:
        larger += 1
    
print (smaller,larger)