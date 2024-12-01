a,b= [int(x) for x in input().split()]
ok=0
for i in range(b-1, a, -1):
    if i % 3 ==0:
        print(i, end=" ")
        ok=1
if ok==0:
    print("NOT FOUND")