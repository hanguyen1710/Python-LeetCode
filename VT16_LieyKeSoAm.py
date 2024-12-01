lst=[]
lst=[int(x) for x in input().split()]
ok=0
res=[]
for v in lst:
    if v<0:
        res.append(v)
        ok=1
if ok==0:
    print("NOT FOUND")
else:
    for v in res:
        print(v, end=" ")