month, year = [int(x) for x in input().split()]
if year <=0 or year > 100000:
    print("INVALID")
else:
    if month >=13 or month < 0 :
        print("INVALID")
    elif (year % 400 ==0) or (year % 4==0 and year % 100 !=0):
        if month == 2 :
            print("29")
        elif month == 1 or month == 3 or month == 5 or month ==7 or month == 8 or month == 10 or month ==12:
            print("31")
        else:
            print("30")
    else:
        if month == 2 :
            print("28")
        elif month == 1 or month == 3 or month == 5 or month ==7 or month == 8 or month == 10 or month ==12:
            print("31")
        else:
            print("30")
    
            
        
        