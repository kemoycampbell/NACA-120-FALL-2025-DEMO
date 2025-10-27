tasks = []

def menu_options():
    menus = [
        "Add a task",
        "Removing a task",
        "Searching task",
        "Updating a task",
        "View done tasks",
        "Sorting tasks"
        ]

    #show the menu
    print("menu\n======")
    for index in range(len(menus)):
        print(str(index+1)+"."+menus[index])

def prompt_for_task():
    while True:
        task_name = input("Enter the name of the task:")
        #check for empty
        if task_name == "":
            print("Task name cannot be empty!")
            continue

        #add the name of the task and its status
        #new tasks are automatically todo
        new_task = task_name + ",todo"
        tasks.append(new_task)
        print(new_task+" was added to the list")
        break

def search_for_task(task_name):
    #search in tasks list
    match_found = False
    for task_status in tasks:
        #split up the name of the task and status
        info = task_status.split(",")
        task = info[0]
        if task == task_name:
            print("Match was found!")
            print("Result:", info)
            match_found = True
            break
    if match_found == False:
        print("No match was found")


while True:
    menu_options()
    #ask the user to select
    selection = int(input("Enter a option:"))
    if selection < 1 or selection > 6:
        print("Please enter 1-6")
        continue
    if selection == 1:
        prompt_for_task()
    elif selection == 3:
        task_name = input("Enter the name of the task to search:")
        search_for_task(task_name)

