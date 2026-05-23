#Cho file input.txt gồm các kiểu dữ liệu chữ và số. Lập trình output.txt (gồm outso.txt và outchu.txt)
tep_vao = open("input.txt", "r", encoding = "utf-8")
du_lieu = tep_vao.read()
tep_vao.close()
danh_sach_so = " "
danh_sach_chu = " "
for ky_tu in du_lieu:
    if ky_tu.isdigit():
        danh_sach_so = danh_sach_so + ky_tu
    if ky_tu.isalpha():
        danh_sach_chu = danh_sach_chu + ky_tu
tep_so = open("outso.txt", "w", encoding = "utf-8")
tep_so.write(danh_sach_so)
tep_so.close()
tep_chu = open("outchu.txt", "w", encoding = "utf-8")
tep_chu.write(danh_sach_chu)
tep_chu.close()
print("Da tach xong so va chu")