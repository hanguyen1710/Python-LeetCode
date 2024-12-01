import math
a,b=[int(x) for x in input().split()]
if b==0:
    print("INVALID")
else:
    if a < 0 and b <0 :
        a= abs(a)
        b= abs(b)
        x= math.gcd(a,b)
        x11= a // x
        x22= b // x
        if x22==1:
            print(x11)
        elif x22 == -1:
            print(-x11)
        else:
            print(x11, x22)
    else:
        x= math.gcd(a,b)
        x11= a // x
        x22= b // x
        if x22==1:
            print(x11)
        elif x22 == -1:
            print(-x11)
        else:
            print(x11, x22)