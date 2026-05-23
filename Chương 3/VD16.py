fo = open("foo.txt", "w")
fo.write("Python la ngon ngu lap trinh tuyet voi. \nMinh cung nghi nhu the! \n")
fo.close()

fo = open("foo.txt", "w")
print("Ten cua file la: ", fo.name)
print("File da duoc dong hay chua: ", fo.closed)
print("Che do truy cap la: ", fo.mode)