n= int(input())
sum=0
for i in range(1, 3*n+2):
    if i%2==0:
        sum-=i
    else:
        sum+=i
print(sum)