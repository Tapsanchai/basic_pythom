# set datetime
import datetime
re_datetime = datetime.datetime.now()
print(re_datetime)  # show now datetime
print(re_datetime.strftime("%Y-%m-%d")) # y-m-d
print(re_datetime.strftime("%x"))  # m/d/y
print(re_datetime.strftime("%c"))  # date m day time y
print(re_datetime.strftime("%H:%M:%S %p")) # Time h:m:s (p)
print(re_datetime.strftime("%a %A")) # date
print(re_datetime.strftime("%w")) # number of date
print(re_datetime.strftime("%d %B %Y")) # วันที่ เดือน ปี
print(re_datetime.strftime("%d/%m/%y")) # วันที่ เดือน ปี