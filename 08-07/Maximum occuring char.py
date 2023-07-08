s="testsample"        
counter = []
new_s = sorted(set(s))
        
for i in range(len(new_s)):
    counter.append(s.count(new_s[i]))
            
max_char = max(counter)


for i in range(len(counter)):
    if counter[i] == max_char:
        max_char = counter.index(counter[i])
        
        print (new_s[max_char])     