t= int(input())
while t!=0:
    n= int(input())
    sum=0
    while n!=0:
        sum+=n%10
        n//=10
    t-=1
    print(sum)