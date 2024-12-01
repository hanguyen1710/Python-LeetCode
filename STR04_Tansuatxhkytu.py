s=input()
s=s.lower()
s= sorted(s)
c=[s[0]]
d=[]
for i in range(0, len(s)):
    if (s[i] != c[-1]) and (s[i].isalnum() or s[i].isalpha()):
        c.append(s[i])
        d.append(s.count(s[i]))
c.reverse()
c.pop()
c.reverse()
for i in range(0, len(c)):
    print(c[i], d[i])