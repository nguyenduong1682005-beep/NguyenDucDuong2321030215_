#Đọc vào 1 dãy số từ tệp dulieu.txt (đã tạo ở vd11). Tính và in ra tổng của dãy số đó
f = open("C:\\dulieu.txt", "r")
s = f.read()
s = s.strip()
a = s.split(" ")
t = 0
print("Day so doc duoc la: ", a)
for i in a:
    t = t + int(i)
print("Tong cua day so la: ", t)