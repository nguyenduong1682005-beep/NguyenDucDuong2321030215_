import mymath2
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong hai so la: ", mymath2.cong(x,y))
print("Hieu hai so la: ", mymath2.tru(x,y))
print("Tich hai so la: ", mymath2.nhan(x,y))

#lenh from..import
from mymath2 import cong, tru
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong hai so la: ", cong(x,y))
print("Hieu hai so la: ", tru(x,y))

#lenh from...import*
from mymath2 import*
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong hai so la: ", cong(x,y))
print("Hieu hai so la: ", tru(x,y))
print("Tich hai so la: ", nhan(x,y))
print("Thuong hai so la: ", chia(x,y))