t=int(input())
while t!=0:
    s= input()
    s=s.split()
    for i in range(0, len(s)):
       s[i]= s[i].capitalize()
    for v in s:
        print(v, end=" ")
    t-=1