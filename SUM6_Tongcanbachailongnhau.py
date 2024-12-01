import math
def Tong(n, sum):
    if n < len(sum):
        return sum[n]
    kq= sum[-1]
    for i in range (len(sum), n+1):
        kq= math.sqrt(2+kq)
        sum.append(kq)
    return kq
sum=[0,math.sqrt(2)]
t=int(input())
while t!=0:
    n=int(input())
    kq= Tong(n,sum)
    print("{:.5f}".format(kq))
    t-=1
    