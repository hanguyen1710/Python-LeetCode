#In ra cac chu cai trong khoang 2 ki tu cho trc
a,b=[x for x in input().split()]
a= a.upper()
b=b.upper()
for i in range(ord(a), ord(b)+1):
    print(chr(i), end=" ")
 # Ham ord() -> Tra ve ma ASCII tuong ung voi ki hieu do. Vi dụ x= ord(A) thi x= 65
 # Ham chr() -> Tra ve ki tu tuong ung voi ma ASCII. Vi du x= chr(65) thi x = A
 # Ham upper() -> Tra ve ki tu in hoa tuong ung voi ki tu do