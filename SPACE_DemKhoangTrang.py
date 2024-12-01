t= int(input())
while t!=0:
    lst= input()
    k=lst.split()
    x=len(k)
    if lst[0]== " ":
        if lst[-1] == " ":
            print(x+1)
        else:
            print(x)
    else:
        if lst[-1] == " ":
            print(x)
        else:
            print(x-1)
    

    t-=1
