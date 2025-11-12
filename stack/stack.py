# a empty stack list
#initalize the stack to empty list
stack = []
top = -1 #we use -1 to represent an initalize stack/empty


"""
    This function will return True if the stack
    is empty. False otherwise(if not empty)
"""
def empty():
    if top == -1:
        return True
    else:
        return False

def push(element):
    #add the element to the "end" of the list
    stack.append(element)
    global top
    top = top + 1

def size():
    return top + 1
    #return len(stack) - option 2

"""
    Show what is on the top without removing it
"""
def peek():
    if empty():
        raise Exception("The stack is empty")
    else:
        return stack[top]

"""
    show what is on the top without remove it
"""
def top():
    return peek()

"""
    remove and return the element from the top of the stack
"""
def pop():
    global top
    top_element = stack.pop(top)
    
    top = top -1
    return top_element


#Testing
print(f"The size of the stack is:{size()}")
print(f"Is the stack empty:{empty()}")
print("Pushing element: 5 on the stack")
push("5")
print(f"Is the stack empty:{empty()}")
print(f"The size of the stack is:{size()}")
print("Pushing element 7 on the stack")
push(7)
print(f"The size of the stack is:{size()}")
print(f"The element on the top of the stack is:{peek()}")
print(f"Remove the top element:{pop()}")
print(f"The size of the stack is:{size()}")
print(f"The element on the top of the stack is:{peek()}")
