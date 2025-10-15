"""
    This function takes two numbers,
    add them and return the result
    parameters:
        num1 - The first number
        num2 - The second number
    return: the sum of both numbers
"""
def add(num1, num2):
    return num1 + num2

print(add(5,6))

def main():
    #Ask for two numbers from the user
    num1 = input("Enter num1:")
    num2 = input("Enter num2:")
    
    #add the numbers by using the add function
    result = add(num1, num2)
    #show the result to the user
    print("The sum of both number is: ", result)

#invoke/call main
main()