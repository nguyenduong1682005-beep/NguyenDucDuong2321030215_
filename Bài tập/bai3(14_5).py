#Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó kiểm tra xem a có chia hết cho chữ số nhỏ nhất của b hay không
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
b = abs(b)
min_digit = 9
while b > 0:
    digit = b % 10
    if digit < min_digit:
        min_digit = digit
    b = b//10
print("chu so nho nhat cua b:", min_digit)
if min_digit != 0 and a % min_digit == 0:
    print(" a chia het cho chu so nho nhat cua b")
else:
    print("a khong chia het cho chu so nho nhat cua b")