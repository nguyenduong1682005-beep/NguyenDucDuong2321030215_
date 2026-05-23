#Giải hpt: ax + b = 0 (a, b nhập từ bàn phím)
a = float(input("Nhap he so a = "))
b = float(input("Nhap he so b = "))
if (a == 0):
    if (b == 0):
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x = -b/a
    print("x=", x)