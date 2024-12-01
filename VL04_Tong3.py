n=int(input())
sum=0
for i in range(2,n+1):
    sum+=1/i
print("{:.4f}".format(sum))