S="geeksogeeks"
a = []
d = {}
for i in S:
    if i not in d:
        d[i] = 1
    else :
        d[i] += 1
for i in d:
    a.append(d[i])
count = 0
for i in a:
    if i % 2 == 1 :
        count = count+1
if count >1:
    print (False)
else :
    print (True)