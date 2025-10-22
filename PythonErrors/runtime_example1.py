def subtract(num1, num2):
    return num1- num2

def main():
    number1 = input("Enter the first number:")
    number2 = input("Enter the second number:")

    result = subtract(number1, number2)
    print("The result of  "+str(number1) + "-" + str(number2)+ "="+str(result))


main()