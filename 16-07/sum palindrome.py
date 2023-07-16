n = 23
num = int(str(n)[::-1])
flag = False

if n == num:
    print(n)
    flag = True

for i in range(5):
    num = int(str(n)[::-1])
    a = num + n
    b = int(str(a)[::-1])
    
    if a == b:
        print(a)
        flag = True
        break

if not flag:
    print("No palindrome sum found.")
