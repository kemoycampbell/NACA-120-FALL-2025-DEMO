while True:
    try:
        num = input("Enter a number:")
        num = int(num)
        print("You entered " + str(num))
    except:
        print("Please enter a valid number")
