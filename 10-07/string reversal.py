s="GEEKS FOR GEEKS"
s = s[::-1]
result= ""
for i in s:
    if i not in result:
        result=result+i
print (result.replace(" ",""))

