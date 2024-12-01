n=int(input())
lst=[]
lst=list(map(int, input().split()))
lst.sort()
if lst[0] <0 and lst [1] < 0:
    if lst[0] * lst[1] > lst[-2] * lst[-1]:
        print(lst[0] * lst[1])
    else:
        print(lst[-1] * lst[-2])
else:
    print(lst[-1] * lst[-2])