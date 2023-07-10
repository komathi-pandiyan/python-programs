s="abEkipo"
vowels="aeiouAEIOU"
result=""
for i in s:
    if i in vowels:
        result=result+i
    if len(result)>0:
        print (result)   
    else:
        print ("No Vowel")
           