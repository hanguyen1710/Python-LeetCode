import math
x= input()
xx= float(x)
xx1= math.ceil(xx)
xx2= math.floor(xx)
if abs(xx-xx1) <= abs(xx-xx2) :
    print(xx1)
else :
    print(xx2)