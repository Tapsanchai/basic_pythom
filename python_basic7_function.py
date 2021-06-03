#  Create Function
def ShowMessage():
    print("***Welcome to Program***")


ShowMessage()
"""
number = int(input("Enter number: ")) 
def Calculator(n):
    sum = n + 2
    print("Sum =", sum)
Calculator(number)
"""
# argument -> number
# parameter -> n

# tuple argument to function | *args


def add(*args):
    sum = 0
    print(args, "->", type(args))
    new_list = list(args)
    print(args, "->", type(new_list))
    for i in range(len(new_list)):
        sum += new_list[i]
    print("Sum =", sum, "\n")


add(1, 3, 5, 7, 9)

# keyword argument | default parameter


def DisplayName(fname, lname, city="bkk"):
    print("ชื่อ:", fname, " นามสกุล:", lname, " เมือง:", city)


DisplayName(lname="parew", fname="Kuma")
print("")

# list datatype argument to function
d_list = [1, 6, 7, 10]
print("list = ", d_list)


def CheckList(items):
    for i in items:
        print(i, " ", end="")
    print("")
    print("มีค่า 5 ที่ค้นหา") if 5 in items else print("ไม่มีค่า 5 ที่ค้นหา")
    print("")


CheckList(d_list)

# return function
x = "100"


def Rotery(x):
    if len(x) > 3:
        print("ข้อมูลไม่ถูกต้อง")
        return "error"
    else:
        if x == "100":
            print("คุณถูกรางวัล")
            return 1000
        else:
            print("คุณไม่ถูกรางวัล")
            return 0


result = Rotery(x)
if result != "error":
    print("เงินรางวัล =", result)
else:
    print("โปรดตรวจสอบและลองใหม่")
print("")

# dict argument to function | **kwargs


def CreateAccount(**dict_user):
    print("account =", dict_user, "->", type(dict_user))


CreateAccount(name="parew", age="23")
CreateAccount(name="yohoho", age="99", city="bkk")
print("")

# function call function
num2 = 5


def Process1(x, y, z):
    set1 = x + y
    print("[set1] ", x, "+", y, "=", set1)
    return Process2(set1, z)


def Process2(st1, st2):
    sum = st1 * st2
    print("call func success!")
    print("st1 =", st1, "st2 =", st2)
    return sum, st1, st2


show_result = Process1(4, 2, num2)
print(show_result[1], "x", show_result[2], "=", show_result[0], "\n")

# recursive function (ฟังก์ชันที่สามารถทำงานซ้ำๆได้โดยการเรียกใช้งานตนเอง)
re_num = 1


def a(number):
    if number <= 5:
        print("re_num =", number)
        number += 1
    else:
        print("End")
        return
    a(number)  # call func again

a(re_num)
print("")

# set and create factorial function
fac_num = 5
print("Number:",fac_num)
def SetFactorial(number):
    print(number,end=" ") if number == 1 else print(number,"x",end=" ")
    if number == 1:
        return number
    else: 
        result = number * SetFactorial(number-1) # call func again
        return result

    """
    sum = 1
    print("Number: ",number)
    for i in range(1,number+1):
        sum *= i
        if i == 5:
            print(i,end=" ")
        else:
            print(i,"x",end=" ")
    print("")
    
    return sum
    """
result_fac = SetFactorial(fac_num)
print("")
print("5! =", result_fac,"\n")

# lambda function
test_argument_lambda = 5
print("Number to Pow: ",test_argument_lambda)
test_lambda = lambda x : (x ** 2)
print("result: ",test_lambda(test_argument_lambda))