#import stack2
from stack2 import *

def build_pringle(size):
    for chip in range(size,-1,-1):
        print(f"Adding chip:{chip} to the pringle can")
        push(chip)

def is_pringle_all_eaten():
    return empty()

def eat_pringle():
    return pop()

def remaining_pringles():
    return size()

build_pringle(20) #setup a stack with 20 chips

# print(f"All pringle eaten:{is_pringle_all_eaten()}")
# print(f"Eat 1 pringle... the chip i eat is chip#:{eat_pringle()}")
# print(f"Remaining pringles in the can:{remaining_pringles()}")


#eat as long as the pringle is not empty
while not is_pringle_all_eaten():
    print(f"Remaining pringles in the can:{remaining_pringles()}")
    print(f"Eating chip:{eat_pringle()}")

    if is_pringle_all_eaten():
        print("You have ate all chips!")