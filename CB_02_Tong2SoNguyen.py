# Nhap tren cung 1 dong
# split() -> tach chuoi dau vao thanh x cai
# Vi du : co 2 dau vao la a,b thi split() se tach lan nhap dau tien va duy nhat thanh 2 so a, b theo dau cach 
a, b= [int(x) for x in input().split()]
if (a and b) >= -1000 and (a and b) <= 1000 :
    print(a+b)