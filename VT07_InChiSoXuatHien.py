lst=[int(x) for x in input().split()]
x=lst[-1]
res=[]
ok=0
for i in range(0,10):
    if lst[i]==x:
        res.append(i+1)
        ok=1
if ok==0:
    print("-1")
else:
    for v in res:
        print(v, end=" ")