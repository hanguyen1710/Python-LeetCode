import math
def isprime (n):
    if n < 2:
        return False
    else:
        x= math.sqrt(n)
        for i in range(2,int(x)+1):
            if n % i ==0:
                return False
        return True

n= int(input())
lst=[]
lst=list(map(int, input().split()))
lst=set(lst)
res=[]
for v in lst:
    if isprime(v):
        res.append(v)
res.sort()
for x in res:
    print(x, end=" ")
