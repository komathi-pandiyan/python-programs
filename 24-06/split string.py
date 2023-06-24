S= "geeks01$$for02geeks03!@!!"
alpha = ""
num = ""
special = ""
for i in range(len(S)):
    if (S[i].isdigit()):
        num = num+ S[i]
    elif((S[i] >= 'A' and S[i] <= 'Z') or (S[i] >= 'a' and S[i] <= 'z')):
    	alpha += S[i]
    else:
    	special += S[i]
print(alpha)
print(num )
print(special)