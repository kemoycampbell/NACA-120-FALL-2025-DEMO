
#set up a empty list to hold our queue elements
queue = []



def peek():
    if empty():
        raise Exception("The queue is empty!")
    
    return queue[0] #return what is at the front (FIFO cares about front)



def enqueue(element):
    queue.append(element)

def dequeue():
    if empty():
        raise Exception("The queue is empty!")
    return queue.pop(0) #remove the element at the front of the list

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return True
    return False

# print(f"Is the queue empty:{empty()}")
# print(f"Queue size:{size()}")
# print("Adding Analiese to the queue")
# enqueue("Analiese")
# print("Adding Ahmed to the back")
# enqueue("Ahmed")
# print(f"The element at the front is: {peek()}")
# print(f"Queue size:{size()}")
# print(f"Processing the front element:{dequeue()}")
# print(f"The new element at the front now is:{peek()}")
# print(f"Queue size:{size()}")
