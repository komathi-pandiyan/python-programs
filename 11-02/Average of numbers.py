size=int(input("Enter the number of elements you want in array: "))
arr=[]
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
avg=sum(arr)/size
print("Average of the array elements is ",avg)