print("**** Convert Temp Program ****")
print("Choose 1 = Celsius to Fahrenheit")
print("Choose 2 = Fahrenheit to Celsius")
choose_one = int(input("Please Choose (1 OR 2):"))
if choose_one == 1 or choose_one == 2:
    if choose_one == 1:
        temp = float(input("Enter your temperature(C): "))
        result = 9/5*temp+32
        unit = "ฟาเรนไฮน์"
    else:
        temp = float(input("Enter your temperature(F): "))
        result = (5/9)*(temp-32)
        unit = "เซลเซียส"
    tem_show = "แปลงอุณหภูมิ {0} เป็น {1:.2f} {2}"
    print(tem_show.format(temp,result,unit))
else:
    print("You Not Choose Only 1 OR 2!!")