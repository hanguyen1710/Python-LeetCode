from math import factorial
x,n= [int(x) for x in input().split()]
res=0
for i in range(1,n+1):
    res += (x**i)/ (factorial(i))
print("{:.2f}".format(res))