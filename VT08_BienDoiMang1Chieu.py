n=int(input())
lst=[]
lst= list(map(int,input().split()))
for i in range(0,n):
    if i % 2 !=0:
        if i < n-1 and i >0:
            lst[i]= lst[i] + abs(lst[i-1] - lst[i+1])
        elif i == n-1:
            lst[i]= lst[i] + lst[i-1] + 0
        else:
            lst[i]= lst[i]  + lst[i+1]
for v in lst:
    print(v, end=" ")