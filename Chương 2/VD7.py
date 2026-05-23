#Giải hpt: ax + b = 0 (a, b nhập từ bàn phím)
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
if (a == 0) and (b == 0):
    print("Phuong trinh vo so nghiem")
elif (a == 0) and (b != 0):
    print("Phuong trinh vo nghiem")
else:
    x = -b/a
    print("x=", x)