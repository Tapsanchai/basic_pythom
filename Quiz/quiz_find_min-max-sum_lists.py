number_list =[]
for i in range(1,5+1):
    number = int(input("Enter Number: "))

    number_list.append(number)

print("number_list =", number_list)
number_list.sort()
print("จัดเรียงใหม่ =", number_list) 
print("Min of number_list =", min(number_list))
print("Max of number_list =", max(number_list))
print("Sum of number_list =", sum(number_list))