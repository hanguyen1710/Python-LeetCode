import math
def cs(n):
    cs=0
    while n!=0:
        cs+=1
        n //=10
    return cs

t= int(input())
while t!=0:
    n= int(input())
    print(cs(math.factorial(n)))
    t-=1