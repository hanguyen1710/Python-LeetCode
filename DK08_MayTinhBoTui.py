x= input()
a,c,b= x.split()
a= float(a);
b= float(b)
if c== '+':
    print("{:.2f}".format(a + b))
elif c == '-':
    print("{:.2f}".format(a - b))
elif c == '*':
    print("{:.2f}".format(a * b))
else:
    if b == 0:
        print("Math Error")
    else:
        print("{:.2f}".format(a / b))