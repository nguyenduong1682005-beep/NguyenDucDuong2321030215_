#viết chương trình nhập vào 1 dãy số thực x1, x2,..xn 90 < x < 100) sau đó tìm trung bình cộng các phần tử dương trong dãy mà giá trị nằm trong khoảng (0, 1000)
a = []
n = int(input("Nhap so phan tu cua day so: "))
for i in range(1, n+1):
    k = float(input("Nhap phan tu thu" + str(i) + ":"))
    a.append(k)
tong = 0
dem = 0
for i in a:
    if 0 < i < 1000:
        tong += i
        dem +- 1
if dem > 0:
    print("Trung binh cong = ", tong/dem)
else:
    print("Khong co phan tu thoa man")