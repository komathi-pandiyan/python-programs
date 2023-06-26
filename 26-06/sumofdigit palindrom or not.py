N=56
total=0
while N>0:
    digit=N%10
    total=total+digit
    N=N//10
string=str(total)
string_rev=string[::-1]
if string==string_rev:
    print(1)
else:
    print(0)
    