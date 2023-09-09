mlist=[]
number=int(input("how item:"))

for n in range(number):
    n=int(input("enter {} item :". format(n)))
    mlist.append(n)

print("my list before sort:",mlist)

for m in range(len(mlist)-1):
    for o in range(0,len(mlist)-m-1):
        if mlist[o]>mlist[o+1]:
            temp=mlist[o]
            mlist[o]=mlist[o+1]
            mlist[o+1]=temp
print("my list after shoting:",mlist)