def Nhap(m,n,a):
    hang=[]
    cot=[]
    for i in range(0,m):
        cot=a[i*n: (i+1)*n]
        if not cot:
            break
        hang.append(cot)
    return hang

m,n,i=[int(x) for x in input().split()]
a= [int(x) for x in input().split()]
hang= Nhap(m,n,a)
hang[i-1]= sorted(hang[i-1])
for v in hang:
    for x in v:
        print(x, end=" ")
    print()
