#Nhập vào dãy số khác 0. Tính tổng các số chẵn
s = input("Nhap day so: ")
ds = list(map(int, s.split()))
i = 0
tong = 0
while i < len(ds):
    if ds[i] % 2 == 0:
        tong += ds[i]
    i += 1
print("Tong cac so chan: ", tong)