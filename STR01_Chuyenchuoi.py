x= input()
y= len(x)
lst=[]
# Ham ord() -> Tra ve ma ASCII tuong ung voi ki hieu do. Vi dụ x= ord(A) thi x= 65
# Ham chr() -> Tra ve ki tu tuong ung voi ma ASCII. Vi du x= chr(65) thi x = A
# Ham upper() -> Tra ve ki tu in hoa tuong ung voi ki tu do
for i in range(0, y):
    if x[i] == x[i].upper():
        a=x[i].lower()
        lst.append(a)
    else:
        lst.append(x[i])
for v in lst:
    print(v, end="")
    
    
