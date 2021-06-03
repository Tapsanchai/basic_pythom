# print & set variables 
"""
คอมเม้นใหญ่

"""
print("hello")
v_str = "Parew"
v_flt = 5.456
v_num = 789
v_bool = True
v_array = [v_str, v_flt, v_num, v_bool]
print(v_array, "=" ,type(v_array))
print("v_array[1] * v_array[2] =", float(v_array[1] * v_array[2]), "\n")

# convert type variables
con_v = int(v_flt);
sum = con_v + v_num
print("{v_flt} =", v_flt)
print("{v_flt} convert to Int =", con_v)
print(con_v, "+", v_num, "=", sum, "\n")

# function input stream
"""
yourname = input("Enter your name: ")
num1 = int(input("Number1 :"))
num2 = int(input("Number2 :"))
sum2 = num1 + num2
print("Wellcome, Mr.", yourname)
print("num1 + num2 =", sum2)
"""

# if-else
"""
age = int(input("Enter your age: "))
if age >= 18:
    print("คุณสามารถเข้าดูได้")
elif age < 18:
    print("คุณอายุต่ำกว่า 18 ปี!!")
else:
    print("คุณกรอกข้อมูลไม่ถูกต้อง โปรดลองใหม่..")
"""

# if-else termary operator
code = '001'
print(code, "\n") if code == '001' else print("error", "\n")

#acession index of string
name_full = "Kuma Parew"
print(name_full)
print(name_full[:5])
print(name_full[5:10])
print(name_full[:-1])
# นับจำนวนตัวอักษรทั้งหมดในชุดข้อมูล
print("จำนวนตัวอักษร =", len(name_full))
name_full2 = "  Kuma Parew  "
print(name_full2)
# ลบช่องว่างออก ทั้งหน้าสุดและหลังสุด
print("ลบช่องว่าง =", name_full2.strip())
# ทำให้เป็นตัวพิมพ์ใหญ่ทั้งหมด
print(name_full2.upper())
# ทำให้เป็นตัวพิมพ์เล็กทั้งหมด
print(name_full2.lower())
name_full3 = "test"
print(name_full3)
# ทำให้เป็นตัวอักษรตัวแรกขึ้นต้นด้วยตัวพิมพ์ใหญ่
print(name_full3.capitalize())
# การแทนที่ข้อความ
print(name_full.replace("Parew","Mee"))
txt1 = "Hi, My name is Parew."
# ตรวจข้อความ ว่ามีคำหรือข้อความที่ต้องการค้นหาหรือไม่
clicked = "name" in txt1
# ถ้ามีข้อความที่ต้องการค้นหา ให้แทนที่ข้อความ แต่ถ้าไม่มี ให้แสดงว่าไม่มีข้อความที่ค้นหา
print("มีข้อความที่ต้องการค้นหา =", clicked) ,print("เปลี่ยนข้อความ name => Name555", txt1.replace("name","Nmae555"), "\n") if (clicked) else print("ไม่มีข้อความที่ค้นหา", clicked, "\n")
# การจัดรูปแบบข้อความ โดยการนำข้อมูลไปแสดงใน เทมเพจข้อความที่สร้างไว้
fname_lname = "Thapsaenchai Chasanguan"
grade = 3.5
salary = 28700.45616847
tem_txt = "ชื่อ:{0}\t เกรด:{1}\t อาชีพ:{2}\t เงินเดือน:{3:.3f}\t"
print(tem_txt.format(fname_lname,grade,"Python Developer",salary))
# การนับจำนวนคำหรือประโยคที่ต้องการค้นหา ในชุดข้อความ
zoo_txt = "dog cat dog"
print(zoo_txt)
print("มีคำว่า 'dog' จำนวน =",zoo_txt.count("dog"), "คำ")
# เช็คคำขึ้นต้นหรือคำนำหน้า
client_name = "Mr.Yohoho"
if client_name.startswith("Mr."):
    print("He is gentlemen.")
else: 
    print("She is Ladies.")
# เช็คคำลงท้าย
rotery = "1545"
print("คุณถูกรางวัล") if rotery.endswith("45") else print("คุณไม่ถูกรางวัล")
