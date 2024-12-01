from math import factorial
n,k=[int(x) for x in input().split()]
res= factorial(n)/(factorial(k) * factorial(n-k))
print(int(res))