n=int(input())
lst=[]
cnt=0
mx= -10**10
idex=-1
while n!=cnt:
    lst=[int(x) for x in input().split()]
    cnt=len(lst)
    if cnt==n:
        break
for i in range(n):
    if lst[i] >= mx:
        mx=lst[i]
        idex=i
print(idex)