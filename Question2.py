m=int(input("enter list item:"))
nlist=[]
for i in range(m):
    temp=int(input("enter {} index in list:".format(i)))
    nlist.append(temp)
print("this list is:", nlist)

def maximum(l):
    max1=l[0]
    for n in l:
        if n>max1:
            max1=n
    print("largest number of evenlist using for loop is:",max1)


def minimum(l):
    min1=l[0]
    for o in l:
        if o<min1:
            min1=o

    print("minimum number of oddlist using for loop is:",min1)

maximum(nlist)
minimum(nlist)