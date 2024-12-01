import math
a,b= [int(x) for x in input().split()]
a= abs(a)
b= abs(b)
if a*b !=0:
    x= (a*b)//math.gcd(a,b)
    print(x)