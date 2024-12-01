def Tong(n, sum):
    if n < len(sum):
        return sum[n]
    kq=sum[-1]
    for i in range(len(sum)*2-1, 2*n, 2):
        kq+= 1/i
        sum.append(kq)
    return kq
sum=[0,1]
t=int(input())
while t!=0:
    n=int(input())
    kq=Tong(n,sum)
    print("{:.5f}".format(kq))
    t-=1