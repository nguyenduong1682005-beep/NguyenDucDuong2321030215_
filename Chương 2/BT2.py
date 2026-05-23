#Nhập vào 1 dãy số tính tổng các chữ số chăn có mặt trong dãy đó
s = input("Nhap day so: ")
tong = 0
i = 0
while i < len(s):
    if s[i].isdigit():
        so = int(s[i])
        if so % 2 == 0:
            tong += so
    i += 1
print("Tong chu so chan: ", tong)