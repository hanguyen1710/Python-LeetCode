a= input()
t= int(input())
while t!=0:
    x= input()
    if x.isupper():
        a=a.upper()
        print(a.count(x))
    else:
        a=a.lower()
        print(a.count(x))
    t-=1