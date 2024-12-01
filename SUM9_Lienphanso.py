def Tong(n,sum):
    if n < len(sum):
        return sum[n]
    kq=sum[-1]
    for i in range(len(sum), n+1):
        kq=1/(1+kq)
        sum.append(kq)
    return kq

t=int(input())
sum=[0,1/2]
while t!=0:
    n=int(input())
    kq= Tong(n,sum)
    print("{:.5f}".format(kq))
    t-=1
        