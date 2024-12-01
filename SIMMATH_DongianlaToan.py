
t=int(input())
cnt= 998244353
while t!=0:
    sum=0
    a,b,c=[int(x) for x in input().split()]
    sum= 1*1*((c*(c+1))//2)
    sum %= cnt
    sum*=(b*(b+1))//2
    sum%= cnt
    sum*= (a*(a+1))//2
    sum%=cnt
    print(sum)
    t-=1
    