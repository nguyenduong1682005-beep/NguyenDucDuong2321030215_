#Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó tính tổng (a+b) và tìm ra chữ số lớn nhất trong tổng đó
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
tong = a+b
print("Tong =", tong)
ds = []
for i in str(tong):
    ds.append(int(i))
print("Chu so lon nhat trong tong la: ", max(ds))