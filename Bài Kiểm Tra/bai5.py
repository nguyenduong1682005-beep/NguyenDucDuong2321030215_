#Viết chương trình nhập vào 2 số nguyên duong m và n, sau đó kiểm tra xem n có chia hết cho tổng các chữ số của n hay không
m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = 0
for i in str(n):
    tong += int(i)
print("Tong cac chu so cua n =", tong)
if m % tong == 0:
    print("m chia het cho tong cac chu so cua n")
else:
    print("m khong chia het cho tong cac chu so cua n")