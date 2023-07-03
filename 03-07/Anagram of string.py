S1 = "bcadeh"
S2 = "hea"
count = 0
for char in S1:
    if char not in S2:
        count += 1
    for char in S2:
        if char not in S1:
            count += 1
print (count)