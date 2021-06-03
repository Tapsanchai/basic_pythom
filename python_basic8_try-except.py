# Try - Except 
'''
try -> ลองทำงานก่อน ถ้าไม่มีข้อผิดพลาด ให้ทำงานปกติ
except -> ถ้ามีข้อผิดพลาดเกิดขึ้นใน try ให้ทำสั่งใน except
'''

try:
    number1 = int(input("enter number:"))
    number2 = int(input("enter number:"))
    print("number1: ", number1)
    print("number2: ", number2)
    sum = number1 * number2
    
    # create your except (กำหนดกฏและออกแบบการตรวจสอบข้อผิดพลาดด้วยตัวผู้เขียนเอง)
    if sum >= 100:
        raise Exception("อย่าหาทำให้ Sum เกินค่า 100!!")
    else:
        print(sum)
# ลดรูปการ except | ตั้งกฏการตรวจสอบไว้กว้างๆ ถ้า error ให้โปรแกรมเป็นคนบอกเอง
except Exception as error:
    print(error)
# else (ถ้าไม่พบปัญหาในโปรแกรม)
else:
    print("success!")
# finally (เมื่อมีข้อผิดพลาด ให้ทำงานคำสั่งอื่นๆ ในส่วนที่ยังทำงานได้)
finally:
    print("KEEP GOING!!")

'''
except ValueError:
    # ถ้าไม่ได้กรอกตัวเลข Integer ให้แสดงข้อความแจ้งเตือน
    print("คุณกรอกข้อมูลไม่ถูกต้อง ")
except TypeError:
    print("ชนิดข้อมูลไม่ตรงกัน ")
except ZeroDivisionError:
    print("ห้ามหารด้วยเลข 0")
'''



