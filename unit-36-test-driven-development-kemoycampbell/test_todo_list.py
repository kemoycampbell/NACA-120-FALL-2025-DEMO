from todo_list import *

def test_get_tasks_size():

    #setup
    expected = 0
    #invoke
    actual = get_tasks_size()

    #analyze
    assert actual == expected

def  test_add_task():

    #setup
    name = "wash the car"

    expected = get_tasks_size() > 0

    #invoke
    add_task(name)

    assert expected == True



