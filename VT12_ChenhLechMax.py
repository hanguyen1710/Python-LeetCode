n=int(input())
lst=[]
lst=list(map(int,input().split()))
lst.sort()
print(lst[-1] - lst[0])