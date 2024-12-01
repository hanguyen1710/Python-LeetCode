def Nhap(n, a):
    hang=[]
    cot=[]
    for i in range(0,n):
        cot=[a[0:n]]
        if a==[]:
            break
        a.reverse()
        for j in range(0, n):
            a.pop()
        a.reverse()
        hang.append(cot)
    return hang
n= int(input())
a=[int(x) for x in input().split()]
sum=0
hang=Nhap(n,a)
v=[]
for i in range(0,n):
    for v in hang[i]:
        sum+=v[i]
print(sum)
