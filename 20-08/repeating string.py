def count_words(string):

    l=string.split()

    s=set(l)

    d={}

    for i in s:

        x=l.count(i)

        d[i]=x

    return d

def max_occurance(string):

    d=count_words(string)

    l1=[]

    for i in d.values():

        l1.append(i)

    max1=max(l1)

    for i in d.keys():

        if d[i]==max1:

            return i

string=input() 

print(max_occurance(string))