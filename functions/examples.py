"""
    This is a function that takes
    two numbers, add their results,
    and return the result
"""
def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    return num1 - num2

#Assigning the result to a variable
sum1 = add(5,6)
print("The result is:",sum1)
#print the result from the function
#without assigning to a variable
print("The result is:", add(5,6))
print("The result of 5-6 is:", subtract(5,6))