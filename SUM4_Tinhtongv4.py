t=int(input())
while t!=0:
    n=int(input())
    sum=1+ 2* (1/2 - 1/(n+1))
    
    print("{:.8f}".format(sum))
    t-=1