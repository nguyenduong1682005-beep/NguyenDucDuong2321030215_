#Đọc vào 1 ma trận từ tệp matran.txt (ở vd12). Tính và in ra tổng của ma trận đó
f = open("C:\\matran.txt", "r")
ma = []
for dong in f:
    if dong[0].isdigit():
        ma.append(dong.split())
print(ma)
s = 0
for i in ma:
    for j in i:
        s += float(j)

print("Tong cua ma tran la: ", s)
f.close()