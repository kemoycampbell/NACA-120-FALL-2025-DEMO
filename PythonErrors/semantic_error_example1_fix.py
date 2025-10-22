def add(num1, num2):
    return num1+ num2

def main():
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))

    result = add(number1, number2)
    print("The result of  "+str(number1) + "+" + str(number2)+ "="+str(result))


main()