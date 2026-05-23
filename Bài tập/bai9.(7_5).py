#Viết chương trình nhập vào 3 số nguyên duong a,b,c sau đó tính tổng (a+b+c) và kiểm tra xem trong tổng đó có bao nhiêu chữ số chẵn
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
tong = a + b + c
print("Tong =", tong)
dem = 0
t = tong
while t > 0:
    digit = t % 10
    if digit % 2 == 0:
        dem +- 1
    t = t //10
print("So chu so chan trong tong la: ", dem)