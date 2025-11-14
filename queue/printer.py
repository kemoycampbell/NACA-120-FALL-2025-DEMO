from queueCustom import *
import time


menu = [
    "Add new document",
    "Print document",
    "Remaining Jobs",
    "Exit"
]


while True:
    print("Menu options\n===============")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
    
    choice = input("Enter your choice:")
    if choice == "1":
        document = input("Enter the name of the document:")
        #add the document to the printer job
        enqueue(document)
        #let the user know the document was added to the printer
        print("The document was added to the printer")
    elif choice == "2":
        if not empty():
            print(f"Printing the document:{dequeue()}")
        else:
            print("There are no jobs in the printer!")
    elif choice == "3":
        print(f"Remaining jobs: {size()}")
    elif choice == "4":
        print("Thank you for using NACA-120 printer!")
        time.sleep(1)
        print("Goodbye.....")
        time.sleep(1)
        print("For real...Goodbye this time....")
        time.sleep(2)
        print("Still here.... :-)....Bye!")
        break
    else:
        print("Really???? What is so hard about picking the right menu option?!")
    
    print("\n")
    