import math
n= int(input())

if n==0:
    print("INF")
elif n<0:
    n= abs(n)
    for i in range(1, n+1):
         if n % i ==0 :
            print (n//i, end=" ")
        
else:
    for i in range(1, n+1):
         if n % i ==0 :
            print (n//i, end=" ")
        