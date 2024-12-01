import math
def scs(n):
    scs=0
    while n!=0:
        scs+=1
        n//=10
    return scs

t= int(input())
while t!= 0:
    n= int(input())
    x=1
    cnt=0
    res=[]
    while cnt < n:
        cnt += math.log10(x)
        if cnt > n-1 and cnt < n:
            res.append(x)
        x+=1
    if len(res) == 0:
        print("NO")
    else:
        print(len(res), end=" ")
        if len(res)==1:
            print(res[0])
        else:
            for i in range(len(res)-1):
                print(res[i], end=" ")
                print(res[-1])
               
    t-=1
