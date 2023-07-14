n=2
for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            for k in range(i):
                print(j, end=" ")
        print("$",end="")
    
        if i == 1:
            print()
