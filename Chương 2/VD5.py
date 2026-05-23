#Nhập vào 2 số x, y. Kiểm tra xem x = y, x > y, x < y hay không
x = float(input("Nhap x: "))
y = float(input("Nhap y: "))
if ( x == y):
    print('x = y')
elif (x > y):
    print('x > y')
else:
    print('x < y')