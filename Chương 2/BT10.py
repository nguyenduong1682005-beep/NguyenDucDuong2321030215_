#Tìm các số hoàn hảo bé hơn 100
n = int(input("Nhap n: "))
for i in range (1, 100):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s = s + j
    if s == i:
        print(i)