x = 1
while x < 13:
    x += 3
    if x % 3 == 0:
        if x%2 == 0:
            x = x+4
            print("111")
            if x % 6 == 0:
                print(x-2)
                x = x - 2
            print("222")
        else:
            x = x-4
            print(x+3)
        print(x)
    else:
        x = x + 1
        if x == 7:
            break
            print("last")
    print("end")
    x -=2
x = x-5
print(x)
print("program end")