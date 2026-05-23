#Sử dụng while để tính tổng các số từ 1 đén n (bới n là 1 số nguyên dương được nhập vào từ bàn phím)
n = int(input("Nhap n: "))
tong = 0
i = 1
while i <= n:
    tong = tong + 1
    i = i + 1
print("Tong la ", tong)