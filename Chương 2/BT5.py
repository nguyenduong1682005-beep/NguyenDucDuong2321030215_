#Viết chương trình nhập 1 dãy số nguyên gồm n phần tử. Tính và in ra tổng các số trong dãy đó
a = []
n = int(input("Nhap so phan tu cua day so: "))
for i in range(1, n+1):
    k = int(input("Nhap phan tu thu" + str(i) + ":"))
    a.append(k)
s = 0
for i in a:
    s = s+i
print("Tong cua day so la: " + str(s))