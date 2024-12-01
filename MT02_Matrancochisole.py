def Nhap(m,n,a):
    hang=[]
    cot=[]
    for i in range(0,m):
        cot=[a[0:n]]
        if a==[]:
            break
        a.reverse()
        for j in range(0,n):
            a.pop()
        a.reverse()
        hang.append(cot)
    return hang
m,n=[int(x) for x in input().split()]
a= [int(x) for x in input().split()]
hang= Nhap(m,n,a)
sum=0
v=[]
for i in range(0,m):
    if i%2!=0:
        for v in hang[i]:
           for x in v:
               sum+=x
    
print(sum)