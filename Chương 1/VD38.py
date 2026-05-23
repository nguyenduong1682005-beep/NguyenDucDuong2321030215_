from datetime import datetime
dt_string = "11/07/2021"
ngay_thang = datetime.strptime(dt_string, "%d/%m/%Y")
print(ngay_thang)
s = ngay_thang.strftime("%d/%m/%y")
print(s)