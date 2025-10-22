def divide(num1,num2):
    return num1/num2

def main():
    number1 = float(input("Enter the first number:"))
    number2 = float(input("Enter the second number:"))
    if number2 == 0:
        print("You cant divide by 0!")
        print("result:0")
    else:
        result = divide(number1, number2)
        print("The result of  "+str(number1) + "/" + str(number2)+ "="+str(result))

main()