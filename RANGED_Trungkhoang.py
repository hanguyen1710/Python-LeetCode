a,b,c,d=[int(x) for x in input().split()]
if a<=c and d >=a:
    print("YES")
elif c >= a and d <= b:
    print("YES")
elif c <= b and d >= b:
    print("YES")
elif c <= a and d >= b:
    print("YES")
elif (a <= c and c <=b) or (a >=c and b <=d) or (a <=d and d<=b) or (a<=c and d <=b):
    print("YES")
else:
    print("NO")