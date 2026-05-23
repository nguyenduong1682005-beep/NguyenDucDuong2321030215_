#Nhập vào 3 điểm toán, lí, hóa và tính điểm trung bình. Kiểm tra xem điểm trung bình < 5: yếu, < 7: trung bình, < 9: khá, còn lại giỏi
i = 0
tong = 0
mon = ['Toan','Li', 'Hoa']
while i < 3:
    diem = float(input(f"Nhap diem{mon[i]}: "))
    tong += diem
    i += 1
dtb = tong/3
print("Diem trung binh: ", dtb)
if dtb < 5:
    print("Yeu")
elif dtb < 7:
    print("Trung binh")
elif dtb < 9:
    print("Kha")
else:
    print("Gioi")