from numbersCustom import *

def test_size():
    #setup
    expected = 0

    #invoke
    actual = size()

    #analyze
    assert actual == expected

def test_push():
    #setup
    number = 5
    expected = 1

    #invoke
    push(number)
    actual = size()

    #analyze
    actual  == expected



