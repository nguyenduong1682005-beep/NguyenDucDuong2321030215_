#Viết chương trình nhập vào 1 số nguyên dương n, kiểm tra xem tích các chữ số của n có phải là số chẵn và lớn hơn 20 hay không
n = int(input("Nhap so nguyen duong n: "))
tich = 1
for i in str(n):
    tich = tich*int(i)
print("Tich cac chu so =", tich)
if tich % 2 == 0 and tich > 20:
    print("Thoa man")
else:
    print("Khong thoa man")