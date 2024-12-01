n=int(input())
lst=[]
lst= list(map(int, input().split()))
x=lst[0]
y= lst[-1]
lst.remove(lst[0])
lst.remove(lst[-1])
lst.sort()
res=[]
res.append(x)
for v in lst:
    res.append(v)
res.append(y)  
for x in res:
    print(x, end=" ")

