#Viết chương trình nhập vào một số nguyên dương n, kiểm tra xem tổng các chữ số của n có phải là số chia hết cho 3 hay không
n = int(input("Nhap so nguyen duong n: "))
tong = 0
for i in str(n):
    tong += int(i)
print("Tong cac chu so =", tong)
if tong % 3 == 0:
    print("Tong cac chu so chia het cho 3")
else:
    print("Tong cac chu so khong chia het cho 3")