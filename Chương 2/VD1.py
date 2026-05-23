#Nhập vào 3 số a, b, c. In ra số lớn nhất/bé nhất
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu haiL "))
c = float(input("Nhap so thu ba: "))
max = a
if (b > max):
    max = b
if (c > max):
    max = c
print("So lon nhat trong 3 so %f, %f va %f la %f" %(a, b, c, max))