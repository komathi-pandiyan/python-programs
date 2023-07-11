s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56"
result=" "
for i in s:
    if i.isdigit():
        result=result+i
    else:
        result=result+" "
    num=result.split()        
print (num)   