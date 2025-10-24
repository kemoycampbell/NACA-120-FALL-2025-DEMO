while True:
    num = input("Enter a number:")
    if not num.isdigit(): #we add a checker to prevent the program from crash
        print("You must enter a number")
        continue

    num = int(num)
    print("You entered " + str(num))
