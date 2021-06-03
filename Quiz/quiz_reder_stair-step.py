Final_round = int(input("Enter Your Number: "))
for i in range(1,Final_round+1):
    for x in range(1,i+1):
        print("* ",end="")
    print("")

for row in range(Final_round):
    for col in range(Final_round):
        print("x ",end="")

    print("")



# triangle pattern
"""
n = 5
k = n - 1

# outer loop to handle number of rows
for i in range(0, n):

    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(0, k):
        print(end=" ")

    # decrementing k after each loop
    k = k - 1

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i+1):
    
        # printing stars
        print("* ", end="")

    # ending line after each row
    print("")
"""