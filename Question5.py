def isPrime(num):
     count=0
     for i in range(2,num):
          if num%i==0:
               count=1
     if count==0:
          print("prime")
     else:
          print("not prime")
mynumber=int(input("enter a number to check is Prime"))
isPrime(mynumber)                         
       