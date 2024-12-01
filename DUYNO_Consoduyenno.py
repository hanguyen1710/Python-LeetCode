lst=[]
while True:
    try:
        #Try: sẽ thực hiện các câu lệnh trên trong Try nếu ko có gì xảy ra
        n=input()
        lst.append(n)
    except EOFError:
        #except: ngoại trừ end of file nghĩa là sẽ kết thúc nhập khi gặp cái này và thực hiên mấy cái ở dưới
        break
for v in lst:
    v = int(v)
    str_v = str(v)
    if str_v[0] == str_v[-1]:
        print("YES")
    else:
        print("NO")
#Ấn Ctrl + Z + Enter để dừng nhập