string = input("Enter a String : ")
result = ''  #empty string
ch = input("Enter a Character : ")
for i in string: 
        if i == ' ':  
            i = ch  
        result += i 
print(“String after removing space with t = ”,result)