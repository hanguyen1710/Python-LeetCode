import math
n=int(input())
def Sang(n):
    p=[1] * (n+1)
    p[0]=0
    p[1]=0
    for i in range(2, int(math.sqrt(n+1))+1):
        if p[i] == 1:
            for j in range(i*i,n+1, i):
                p[j]=0
    return p
# Co the tra ve 1 mang 
p=Sang(n)
for i in range(1,n+1):
    if p[i]==1:
        print(i, end=" ")