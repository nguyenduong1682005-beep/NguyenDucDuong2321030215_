#Viết chương trình nhập vào 1 dãy số nguyên x1, x2,...xn ( 0 < n < 200), tính tổng các phần tử chẵn trong dãy và kiểm tra xem tổng này có chia hết cho 7 và nhỏ hơn 200 hay không
n = int(input("Nhap n:"))
a = []
i = 0
while i < n:
    x = int(input("Nhap x:"))
    a.append(x)
    i += 1
tong = 0
i = 0
while i < n:
    if a[i] % 2 == 0:
        tong += a[i]
    i += 1
print("Tong cac so chan:", tong)
if tong % 7 == 0 and tong < 200:
    print("Tong chia het cho 7 va nho hon 200")
else:
    print("Khong thoa dieu kien")