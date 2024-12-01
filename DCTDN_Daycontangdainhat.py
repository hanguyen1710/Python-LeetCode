n=int(input())
cnt=0
while cnt!=n:
    a=[int(x) for x in input().split()]
    cnt=len(a)
    if cnt==n:
        break
b=[]
c=[]
d=[]
for i in range (0,n):
    ma= a[i]
    cnt2=1
    for j in range(i+1, n-1):
        if a[j] > ma:
            if a[j] < a[j+1]:
                for k in range(j,n):
                    if a[k] > ma:
                        ma=a[k]
                        cnt2+=1
                c.append(cnt2)
            else:
                for k in range(j+1,n):
                    if a[k] > ma:
                        ma=a[k]
                        cnt2+=1
                c.append(cnt2)
        d.append(max(c))
    b.append(max(d))
    
print(max(b))
