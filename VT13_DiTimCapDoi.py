n=int(input())
lst=[]
lst=list(map(int, input().split()))
mx= -10**10
sum=-10**10
x=-10**10
y=-10**10
for i in range(0,n):
    if i<n-1:
        sum=lst[i] + lst[i+1]
        if sum >= mx:
            mx=sum
            x=lst[i]
            y=lst[i+1]
    else:
        sum=lst[-1] + lst[0]
        if sum >= mx:
            mx=sum
            x=lst[-1]
            y=lst[0]
print(x,y)