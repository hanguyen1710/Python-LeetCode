import math
def Sumdiv(n):
    sum=0
    x= int(math.sqrt(n))
    for i in range(1,x+1):
        if n%i==0:
            sum+=i
            if n//i != i:
                sum+=n//i
    return sum

t=int(input())
while t!=0:
    n=int(input())
    print(Sumdiv(n))
    t-=1