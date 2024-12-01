n= int(input())
cnt=0
while cnt != n:
    a = [int(x) for x in input().split()]
    cnt=len(a)
    if cnt == n:
        break
b=sorted(set(a))
if len(b) <=1:
    print("NOT FOUND")
else:
    print(b[len(b)-2])