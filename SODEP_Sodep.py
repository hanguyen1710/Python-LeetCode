def check(n):
    n=str(n)
    v= n[::-1] # Dao nguoc mang
    sum=0
    for i in range(0, len(n)):
        sum+= int(n[i])
    return sum  % 10 == 0 and n==v
a=[]
while True:
    try:
        l,r=[int(x) for x in input().split()]
        a.append(l)
        a.append(r)
    except Exception:
        break

for i in range(0, len(a)//2):
    l=a[i*2]
    r=a[(i*2+1)]
    cnt=0
    for j in range(l, r+1):
        if check(j):
            cnt+=1
    print(cnt)