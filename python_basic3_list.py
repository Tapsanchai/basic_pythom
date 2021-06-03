# Non-Primiitive Datatype (list, tuple, dict, set)

# List (สามารถเปลี่ยนเปลงค่าได้)
data_structure = [456, "parew", True, 3.789]
print(data_structure)
print(data_structure[2:])
data_structure[1] = "parew555"
data_structure[2] = False
print(data_structure, "\n")

StudentName_Lists = ["parew", "yohoho", "kuma", "max"]
print("ชุดข้อมูลรายชื่อนักเรียน: ", StudentName_Lists)
for index, value in enumerate(StudentName_Lists):  # loop แบบแสดง index ด้วย
    print("ตำแหน่งที่ ", index, "=", value)
print("มีข้อมูลดังกล่าวใน StudentName_Lists \n") if "parew" in StudentName_Lists else print("ไม่มีข้อมูลดังกล่าวใน StudentName_Lists \n")

# add value to lists
number_list = [4, 7, 5]
print("Add Before",number_list)
# เพิ่มข้อมูลใหม่ต่อท้าย
number_list.append(1000)
# เพิ่มข้อมูลใหม่แทนที่ข้อมูลเก่า ตามตำแหน่งที่ระบุ
number_list.insert(0,500) #ตำแหน่ง, ค่าข้อมูลใหม่
print("Add After",number_list)

# delete value of lists
number_list.remove(7) #ลบข้อมูลด้วย value
del number_list[1] #ลบข้อมูลด้วย index
number_list.pop() #ลบข้อมูลที่ตำแหน่งสุดท้าย
print("Delete After",number_list, "   // 4 7 1000")

# clear lists
number_list.clear()
print("Clear After",number_list)

# union list groups & extend new lists
number_list2 = [4,1,2,3]
txt_list2 = ["z", "Z", "a", "h"]
all_groups = data_structure + number_list2
print(all_groups)
data_structure.extend(number_list2)
print(data_structure)

# sort & reverse (การจัดการเรียงลำดับของชุดข้อมูล) 
number_list2.sort()
print("เรียงจากน้อยไปมาก: ",number_list2)
number_list2.reverse()
print("เรียงจากมากไปน้อย: ",number_list2)
txt_list2.sort()
print("เรียงจากใหญ่ไปเล็ก: ",txt_list2)
txt_list2.reverse()
print("เรียงจากเล็กไปใหญ่: ",txt_list2)
print("\n")
print(StudentName_Lists)
print(StudentName_Lists[::-1])
StudentName_Lists.reverse()
print(StudentName_Lists)
StudentName_Lists.sort()
print(StudentName_Lists)

show_number_powers = [i**2 for i in number_list2]
print("เดิมๆ ",number_list2)
print("ใหม่ ยกกำลัง 2 ", show_number_powers)