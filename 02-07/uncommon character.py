A = "geeksforgeeks"
B = "geeksquiz"
res = ''.join(sorted(set(A) ^ set(B)))
print(res)