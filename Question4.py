m=int(input("enter list item:"))
nlist=[]
for i in range(m):
     temp=int(input("enter {} index in list:".format(i)))
     nlist.append(temp)

def even_odd(m2):
     evenlist=[]
     oddlist=[]
     for i in m2:
          if i%2==0:
               evenlist.append(i)
          elif i%2!=0:
               oddlist.append(i)
     print("newlist is:",nlist)
     print("even list is:",evenlist)
     print("odd list is:",oddlist)
     return evenlist,oddlist,nlist

even_odd(nlist)