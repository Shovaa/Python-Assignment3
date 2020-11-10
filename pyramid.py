

#for printing left angled triangle :
rows= int(input("Enter the number of row:"))
for row in range(1, rows+1):
    for space in range (1, (rows-row)+1):
        print(" ", end="")

    for symbol in range(1, row+1):
        print("*", end="")

    print ()        