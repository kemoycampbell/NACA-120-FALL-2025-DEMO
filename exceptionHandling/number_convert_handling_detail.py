while True:
    try:
        num1 = input("Enter number 1:")
        num1 = int(num1)
        num2 = input("Enter number 2:")
        num2 = int(num2)
        
        result = num1/num2
        print(result)
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Number 2 cannot be 0!")
    except:
        print("An unexpected error occurred. Please try again")
