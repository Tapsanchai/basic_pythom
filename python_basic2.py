# loop while
import random
sum_sequence = 0
average = 0
i = 1
while i <= 5:
    count_sequence = random.randint(1, 10)
    print("รอบที่", i, "ค่าความถี่ =", count_sequence)
    sum_sequence += count_sequence
    print("ค่าความถี่สะสม =", sum_sequence)
    i += 1
    if i > 5:
        average = sum_sequence/5
        print("ค่าเฉลี่ย =", average, "\n")

# for loop
StudentName_Lists = ["parew", "yohoho", "kuma", "max"]
count = 1
for i in range(2, 11, 2):  # ค่าเริ่มต้น, ค่าสิ้นสุดก่อนจำนวนที่ระบุ, เพิ่มค่าขึ้นที่ละเท่าไหร่
    print("รอบที่:", count, "value =", i)
    count += 1

print("ชุดข้อมูลรายชื่อนักเรียน: ", StudentName_Lists)
for index, value in enumerate(StudentName_Lists):  # loop แบบแสดง index ด้วย
    print("ตำแหน่งที่ ", index, "=", value, "\n")

# continue & break
for x in range(1, 10):
    if x == 3:
        continue
    elif x == 6:
        break
    print("Show =", x)
    
# สุ่มทายลูกเต๋า
for v in range(1,3+1): #3 รอบ
    mynumber_random = random.randrange(1,7) #1-6
    answer = int(input("ทายตัวเลขของลูกเต๋าที่ถูกทอย: "))
    print("คุณทายถูก!! เลขที่ออกคือ ", mynumber_random) if answer == mynumber_random else print("คุณทายผิด!! เลขที่ออกคือ ", mynumber_random)

