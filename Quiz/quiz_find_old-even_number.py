
for i in range(1,4):
    print("Round: ",i)
    number = int(input("Enter Number: "))

    def CheckNumber(n):
        print("เลขคู่") if n%2 == 0 else print("เลขคี่")
    CheckNumber(number)

