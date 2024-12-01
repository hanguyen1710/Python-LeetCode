m,n= [int(x) for x in input().split()]
a=[int(x) for x in input().split()]
hang=[]
cot=[]
for i in range(0,m):
    cot=[a[0:n]]
    if a==[]:
        break
    a.reverse()
    for k in range(0,n):
        a.pop()
    a.reverse()
    hang.append(cot)
for v in hang:
    for u in v[0]:
        print(u, end=" ")
    print()
