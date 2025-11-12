# a empty stack list
#initalize the stack to empty list
stack = []

def empty():
#    if len(stack) == 0:
#       return True
#    else:
#       return False
    if size() == 0:
       return True
    return False

def push(element):
   stack.append(element)

def size():
   return len(stack)

def peek():
   if empty():
        raise Exception("The stack is empty")
   
   top = size() - 1
   return stack[top]

def top():
    return peek()

def pop():
    if empty():
        raise Exception("The stack is empty")
    
    top  = size()-1
    return stack.pop(top)

#Testing
# print(f"The size of the stack is:{size()}")
# print(f"Is the stack empty:{empty()}")
# print("Pushing element: 5 on the stack")
# push("5")
# print(f"Is the stack empty:{empty()}")
# print(f"The size of the stack is:{size()}")
# print("Pushing element 7 on the stack")
# push(7)
# print(f"The size of the stack is:{size()}")
# print(f"The element on the top of the stack is:{peek()}")
# print(f"Remove the top element:{pop()}")
# print(f"The size of the stack is:{size()}")
# print(f"The element on the top of the stack is:{peek()}")