import math
def Tong(n):
    kq=math.sqrt(n)
    for i in range(n-1,0,-1):
        kq=math.sqrt(i+kq)
    return kq
    
t=int(input())
while t!=0:
    n=int(input())
    kq=Tong(n)
    print("{:.5f}".format(kq))
    t-=1