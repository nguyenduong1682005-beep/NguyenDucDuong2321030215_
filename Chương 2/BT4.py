#Viết chương trình nhập 1 số tự nhiên n và tính các giá trị ước sô nguyên tố (tính số các ước nguyên tố khác n)
n = int(input("Nhap n: "))
dem = 0
i = 2
while n > 1:
    if n % i != 0:
        i = i + 1
    else:
        dem = dem + 1
        while n % i == 0:
            n = n//i
print()
print("So cac so nguyen to la: ", dem)