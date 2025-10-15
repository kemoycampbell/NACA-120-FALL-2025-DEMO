def add(num1, num2):
    return num1 + num2

def main():
    #ask the user for two numbers
    #conver the inputs from string to int
    num1 = int(input("Enter  the first number:"))
    num2 = int(input("Enter the second number:"))

    #add the results, the result is also a type int
    result = add(num1, num2)

    #we need to cast num1, num2, and result  to be able to concatenate it to a string
    print("The result of " + str(num1) + "+" + str(num2) + " is "+ str(result) )

#call the main
main()