import math
def snt (n):
    if n<2:
        return 0
    else:
        x= int(math.sqrt(n))
        for i in range(2,x+1):
            if n % i == 0:
                return 0
        return 1
    
n= int(input())
if snt(n) == 0:
    print("NO")
else:
    print("YES")