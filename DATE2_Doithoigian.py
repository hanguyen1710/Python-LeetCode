n= int(input())
h=n//3600
p=(n%3600)//60
g=((n%3600)%60)

if h < 10:
    if p < 10:
        if g <10:
            s= "0"+str(h)+ ":" + "0" + str(p) + ":" + "0" + str(g)
        else:
            s= "0"+str(h)+ ":" + "0" + str(p) + ":"+ str(g)
    else:
        if g <10:
            s= "0"+str(h)+ ":"  + str(p) + ":" + "0" + str(g)
        else:
            s= "0"+str(h)+ ":" +str(p) + ":"+ str(g)
else:
    if p < 10:
        if g <10:
            s= str(h)+ ":" + "0" + str(p) + ":" + "0" + str(g)
        else:
            s= str(h)+ ":" + "0" + str(p) + ":"+ str(g)
    else:
        if g <10:
            s= str(h)+ ":"  + str(p) + ":" + "0" + str(g)
        else:
            s=str(h)+ ":" +str(p) + ":"+ str(g)
print(s)