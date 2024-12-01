t= int(input())
while t!=0:
    x= int(input())
    # format -> Dinh dang so nguyen thanh dang mong muon 
    # Dinh dang so nguyen thanh nhi phan -> x= format(10,"b") thì x= 1010
    # Dinh dang so nguyen thanh hexca -> x= hec(255) thì x= 0xff, còn x= "{:.x}".format(255) thì x=ff
    print(format(x,"b"))
    t-=1