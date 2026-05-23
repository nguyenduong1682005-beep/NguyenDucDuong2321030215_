#Viết chương trình nhập 1 dãy số nguyên gồm n phần tử. In ra lũy thừa 2 của dãy số đó
a = []
n = int(input("Nhap so phan tu day so: "))
for i in range(1, n+1):
    k = int(input("Nhap phan tu: "))
    a.append(k)
for i in a:
    print(i ** 2)