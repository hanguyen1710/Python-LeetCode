n=int(input())
lst=[]
lst= list(map(int, input().split()))
lst.sort()
if lst[0] >=0 and lst[1] >=0:
    tich= lst[-3] * lst[-2] * lst[-1]
else:
    if lst[0]*lst[1]*max(lst[-2],lst[-1]) >= lst[0] * lst[1] * lst[2] and lst[0]*lst[1]*max(lst[-2],lst[-1]) >= lst[-3] * lst[-2] * lst[-1]:
        tich= lst[0]*lst[1]*max(lst[-2],lst[-1])
    else:
        tich= max(lst[0] * lst[1] * lst[2], lst[-3] * lst[-2] * lst[-1])
print(tich)

    
        