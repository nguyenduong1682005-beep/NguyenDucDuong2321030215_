#Viết chương trình nhập vào 1 dãy số thực x1, x2,...xn ( 0 < n < 100), sau đó tìm trung bình cộng các phần tử âm trong dãy mà giá trị nằm trong khoảng (-1000, -10)
n = int(input("Nhap n:"))
i = 0
tong = 0
dem = 0
while i < n:
    x = float(input("Nhap x: "))
    if -1000 < x < -10:
        tong += x
        dem += 1
    i += 1
if dem == 0:
    print("Khong co so thoa dieu kien")
else:
    print("Trung binh cong: ", tong/dem)
