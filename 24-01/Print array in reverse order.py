size=int(input("Enter the number of elements you want in array: "))
arr=[]
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
print("Array in reverse order")
# Reversing the list
for i in range(size-1, -1, -1):     
    print(arr[i],end=' ')