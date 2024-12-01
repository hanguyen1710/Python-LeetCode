a,b,c,d,e,f=[int(x) for x in input().split()]
if a/d == b/e:
    if a/d== c/f:
        print("VOSONGHIEM")
    else:
        print("VONGHIEM")
else:
    vt= a - (b*d)/e
    vp= c - (b*f)/e
    x1=vp/vt
    x= "{:.2f}".format(vp/vt)
    y= "{:.2f}".format((f-d*x1)/e)
    if x == "-0.00" :
        print("0.00",y)
    elif y == "-0.00":
        print(x, "0.00")
    else:
        print(x, y)
        
