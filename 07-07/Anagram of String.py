str1="bcadeh"
str2="hea"
for i in str2:
    if i in str1:
        str1=str1.replace(i,'',1)
        str2=str2.replace(i,'',1)
print (len(str1)+ len(str2))