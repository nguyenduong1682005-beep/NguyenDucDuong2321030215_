#Viết chương trình nhập vào 3 số nguyên duong z, y, z, sau đó tìm xem tích (x*y*z) có mấy chữ số và chữ số lớn nhất bằng bao nhiêu
x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))
tich = x*y*z
print("Tich la: ", tich)
chuoi_tich = str(tich)
print("So chu so cua tich: ", len(chuoi_tich))
print("Chu so lon nhat la: ", max(chuoi_tich))