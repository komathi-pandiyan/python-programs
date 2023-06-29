arr = [ 2, -6 ,3 , 5, 1]
n = len(arr)
for i in range(n):
	count = 0
	for j in range(0, n):
		if arr[j] > arr[i]:
			count = count + 1
						
	if count >= 2 :
		print(arr[i], end=" ")
			