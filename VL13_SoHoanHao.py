n= int(input())
sum=0
if n<=0:
    print("NO")
else:
    for i in range(2, n+1):
        if n % i ==0:
            sum+= n//i
    if sum == n:
        print("YES")
    else:
        print("NO")
    