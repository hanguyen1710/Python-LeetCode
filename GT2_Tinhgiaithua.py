import math
t= int(input())
a= [int(x) for x in input().split()]
b=[]
for i in range(0,t):
    x=math.factorial(a[i])
    b.append(x)
for v in b:
    print(v)
    
