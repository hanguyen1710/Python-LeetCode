def scp(n):
    x= int(n**0.5)
    if x*x==n:
        return True
    else:
        return False

m,n= [int(x) for x in input().split()]
hang=[]

for i in range(0,m):
    cot=[int(x) for x in input().split()]
    hang.append(cot)
b=[]
for i in range(0,m):
    for j in range(0,n):
        b.append(hang[i][j])
b=set(b)
#Dung set de loai bo trung nhau
ok=0
for v in b:
    if scp(v):
        print(v, end=" ")
        ok=1
if ok==0:
    print("NOT FOUND")
