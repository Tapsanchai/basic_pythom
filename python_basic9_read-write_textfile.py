import os
# open|read (เปิดไฟล์)
            # name, mode, format
# chk_file_read = open("./textfile/test_txt1.txt","r",encoding="UTF8")
# print(chk_file_read.read())

# write file (เขียนไฟล์)                            w
'''
chk_file_write = open("./textfile/test_txt1.txt","a",encoding="UTF8")
for text in range(2):
    input_text = input("enter text:")
    chk_file_write.writelines(input_text + "\n")
chk_file_write.close()
print(chk_file_read.read())
'''
# remove | delete file (ลบไฟล์)
path_file = "./textfile/test_txt1.txt"
if os.path.exists(path_file):
    print("เจอ")
    os.remove(path_file)
else:
    print("ไม่เจอ")