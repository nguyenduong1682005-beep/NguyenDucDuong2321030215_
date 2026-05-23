#Cho mã: 1, 2, 3, 4, 5 ứng với dân tộc: Kinh, Tày, Nùng, Thái, Khơ-me. Hãy lập chương trình nhập vào mã dân tộc và hiển thị dân tộc tương ứng
ma = int(input("Nhap ma dan toc: "))
if ma == 1:
    print("Dan toc: Kinh")
elif ma == 2:
    print("Dan toc: Tay")
elif ma == 3:
    print("Dan toc: Nung")
elif ma == 4:
    print("Dan toc: Thai")
elif ma == 5:
    print("Dan toc: Kho-me")
else:
    print("Ma khong hop le")