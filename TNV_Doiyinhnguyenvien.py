n=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in range(0, len(a)):
    b.append(a.count(a[i]))


