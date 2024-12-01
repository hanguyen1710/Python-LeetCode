import math
a=int(input())
pi= math.pi
s1= a**2/2
s2= pi * (a**2)/4
s= 2*s1+ 2*(s2-s1)
print("{:.3f}".format(s))
