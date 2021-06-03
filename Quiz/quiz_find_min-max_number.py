min, max =  0,0
for i in range(1,4):
    number = float(input("Enter Number: "))

    if number > max:
        max = number
    if number < max:
        min = number

print("Max =", max)
print("Min =", min)