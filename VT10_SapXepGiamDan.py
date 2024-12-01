n= int(input())
lst=[]
lst= list(map(int, input().split()))
lst.sort(reverse=True)
for v in lst:
    print(v, end=" ")