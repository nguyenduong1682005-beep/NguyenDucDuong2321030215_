#Viết chương trình nhập vapf 2 số nguyên dương m và n, sau đó tính tổng (a+b) và tìm ra số chữ số lớn nhất trong tổng đó
a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
tong = a+b
print("Tong =", tong)
ds = []
for i in str(tong):
    ds.append(int(i))
print("Chu so lon nhat trong tong la:", max(ds))