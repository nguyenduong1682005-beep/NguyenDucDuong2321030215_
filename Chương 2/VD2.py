#Nhập vào 1 số nguyên. Kiểm tra số nguyên đó là chẵn hay lẻ
n = int(input("Nhap vao 1 so nguyen: "))
if (n % 2 == 0):
    print("So" + repr(n) +" la so chan")
else:
    print("So" + repr(n) + "la so le")