size=int(input("Enter the number of elements you want in array: "))
arr=[]
sum=0
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
print("All even number in array are ")
for i in range(0,size):
    if arr[i]%2!=0:
        print(arr[i],end=' ')