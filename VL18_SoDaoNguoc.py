n= int(input())
m=n
cnt=0
while n!=0:
    cnt+=1
    n//=10
x=0
while m!=0:
    r= m % 10
    x = x + r * (10**(cnt-1))
    cnt-=1
    m//=10
print(x)