from mathCustom import *



"""
    This function will test the add function
"""
def test_add():

    #setup
    num1 = 5
    num2 = 5
    expected = 10

    #invoke
    actual = add(num1, num2)

    #analyze
    assert actual == expected

def test_multiply_int():
    #setup
    number1 = 4
    number2 = 6
    goal = 24

    #invoke
    real_result = multiply(number1, number2)

    #analyze
    assert goal == real_result

def test_multiply_str():
    #setup
    number1 = "4"
    number2 = "6"
    goal = 24

    #invoke
    real_result = multiply(number1, number2)

    #analyze
    assert goal == real_result




