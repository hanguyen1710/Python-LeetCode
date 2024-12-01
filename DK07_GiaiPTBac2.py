import math
a,b,c=[int(x) for x in input().split()]
delta= b**2 - 4*a*c
if a==0:
    if b==0 and c==0:
        print ("WOW")
    elif b!=0 and c==0:
        print("0.00")
    elif b==0 and c!=0:
        print("NO")
    else:
        print("{:.2f}".format(-c/b))
else:
    if delta > 0:
        x1= (-b- math.sqrt(delta))/(2*a)
        x2= (-b + math.sqrt(delta))/(2*a)
        x1_t = "{:.2f}".format(x1)
        x2_t= "{:.2f}".format(x2)
        if x1_t == "-0.00":
            x1_t="0.00"
            if x1_t < x2_t:
                print(x1_t, x2_t)
            else:
                print(x2_t, x1_t)
        elif x2_t== "-0.00":
            x2_t= "0.00"
            if x1_t < x2_t:
                print(x1_t, x2_t)
            else:
                print(x2_t, x1_t)
        else:
            if x1_t < x2_t:
                print(x1_t, x2_t)
            else:
                print(x2_t, x1_t)
        
    elif delta ==0:
        x11 = -b/(2*a)
        x11t = "{:.2f}".format(x11)
        if x11t=="-0.00":
            x11t="0.00"
            print(x11t)
        else:
            print(x11t)
    else:
        print("NO")
        