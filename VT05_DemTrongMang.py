n,k=[int(x) for x in input().split()]
lst=[]
cnt=0
while cnt != n:
    lst=[int(x) for x in input().split()]
    cnt=len(lst)
    if cnt == n:
        break
print(lst.count(k))