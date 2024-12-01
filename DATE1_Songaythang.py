n,y=[int(x) for x in input().split()]
if (y%4==0 and y%100!=0) or (y%400==0):
    a=[31,29,31, 30,31,30,31,31,30,31,30,31]
    b=[31]
    for i in range(0, len(a)-1):
        b.append(b[i] +a[i+1])
else:
    a=[31,28,31, 30,31,30,31,31,30,31,30,31]
    b=[31]
    for i in range(0, len(a)-1):
        b.append(b[i] +a[i+1])
for i in range(0,len(b)):
    if n < b[0]:
        print(n, i+1)
        break
    elif n < b[i]:
        print(n-b[i-1], i+1)
        break