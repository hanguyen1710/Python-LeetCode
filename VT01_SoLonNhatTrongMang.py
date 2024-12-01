n= int(input())
cnt=0
while cnt != n:
    a= [int(x) for x in input().split()]
    cnt= len(a)
    if cnt == n:
        break
print(max(a))
      