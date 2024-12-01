import math
a,b,c=[int(x) for x in input().split()]
if a+b <= c or  b+c <=a or c+a <=b :
    print("NO")
else: 
    p=a+b+c
    k=p/2
    s= math.sqrt (k*(k-a)*(k-b)*(k-c))   
    print(p, "{:.2f}".format(s))
    
    