# List to store tasks with their statuses
tasks = []

# Function to display menu options to the user
def menu_options():
    # List of available menu options
    menus = [
        "Add a task",
        "Removing a task",
        "Searching task",
        "Updating a task",
        "View done tasks",
        "Sorting tasks",
        "view all tasks",
        "exit"
        ]

    # Show the menu header
    print("menu\n======")
    # Loop through the menu options and print each one
    for index in range(len(menus)):
        print(str(index+1)+"."+menus[index])

# Function to prompt user for a new task
def prompt_for_task():
    while True:
        # Ask the user for the task name
        task_name = input("Enter the name of the task:")
        # Check if the user entered an empty string
        if task_name == "":
            print("Task name cannot be empty!")
            continue

        # Add the task name and set status as todo
        # new tasks are automatically todo
        new_task = task_name + ",todo"
        # Append the new task to the tasks list
        tasks.append(new_task)
        # Print confirmation that task was added
        print(new_task+" was added to the list")
        break  # Exit the loop once a task is added

# Function to search for a specific task by name
def search_for_task(task_name):
    # Flag to indicate if a match is found
    match_found = False
    # Loop through each task in the tasks list
    for task_status in tasks:
        # Split the task string into name and status
        info = task_status.split(",")
        task = info[0]
        # Check if the task name matches the user input
        if task == task_name:
            print("Match was found!")
            print("Result:", info)
            match_found = True
            break  # Stop searching after finding a match
    # If no match was found, notify the user
    if match_found == False:
        print("No match was found")

# Function to remove a task by name
def remove_task():
    # Flag to track if task was removed
    removed = False
    # Ask the user for the task name to remove
    task_name = input("Enter the name of the task to remove:")
    # Loop through each task in the list
    for task_status in tasks:
        # Split the task into name and status
        info = task_status.split(",")
        task = info[0]
        # Check if current task matches input
        if task == task_name:
            # Remove the matching task
            tasks.remove(task_status)
            print(task_name+" was removed from the list")
            removed = True
            break  # Stop after removing the task
    # If no task was removed, notify user
    if removed == False:
        print("Task not found in the list")

# Function to update the status of a task
def update_task():
    while True:
        # Ask for the task name to update
        task_name = input("Enter the name of the task to update:")
        # Prevent updating with an empty name
        if task_name == "":
            print("Task name cannot be empty!")
            continue

        # Task name provided, break out of input loop
        break

    # Flag to track if the task was updated
    updated = False
    # Loop through each task by index
    for index in range(len(tasks)):
        # Get the task at current index
        task_status = tasks[index]
        # Split into name and status
        info = task_status.split(",")
        task = info[0]
        status = info[1]
        # Check if names match
        if task == task_name:
            # Ask for new status
            new_status = input("Enter the new status:")
            # Ensure status is not empty
            if new_status == "":
                print("Status cannot be empty!")
            else:
                # Combine task name and new status
                # Replace the old task at same index
                tasks[index] = task_name + "," + new_status
                print("Task updated to:", tasks[index])
                updated = True
                break  # Stop after updating
    # If no update occurred, inform the user
    if updated == False:
        print("Task not found in the list")

# Function to view all tasks with "done" status
def view_done_tasks():
    print("Done tasks:")
    # Loop through the tasks
    for task_status in tasks:
        # Split into task and status
        info = task_status.split(",")
        task = info[0]
        status = info[1]
        # Print only tasks marked as done
        if status == "done":
            print("-", task)

# Function to sort the tasks in ascending or descending order
def sort_tasks():
    # Ask the user for sorting order
    sort_order = input("Enter 'asc' for ascending or 'desc' for descending sort:")
    # Sort in ascending order
    if sort_order == "asc":
        tasks.sort()
        print("Tasks sorted in ascending order")
    # Sort in descending order
    elif sort_order == "desc":
        tasks.sort(reverse=True)
        print("Tasks sorted in descending order")

# Function to display all tasks with their statuses
def view_all_tasks():
    print("All tasks:")
    # Loop through the list of tasks
    for task_status in tasks:
        # Split each task into name and status
        info = task_status.split(",")
        task = info[0]
        status = info[1]
        # Display task name and its status
        print("-", task, ":", status)

# Main function to run the program
def main():
    # Loop indefinitely until user chooses to exit
    while True:
        try:
            print("\n")
            # Display menu options
            menu_options()
            # Ask the user to select an option
            selection = int(input("Enter a option:"))
            # Validate that input is between 1 and 8
            if selection < 1 or selection > 8:
                print("Please enter 1-8")
                continue
            # Option 1: Add a task
            if selection == 1:
                prompt_for_task()
            # Option 2: Remove a task
            elif selection == 2:
                remove_task()
            # Option 3: Search for a task
            elif selection == 3:
                task_name = input("Enter the name of the task to search:")
                search_for_task(task_name)
            # Option 4: Update a task
            elif selection == 4:
                update_task()
            # Option 5: View completed tasks
            elif selection == 5:
                view_done_tasks()
            # Option 6: Sort all tasks
            elif selection == 6:
                sort_tasks()
            # Option 7: View all tasks
            elif selection == 7:
                view_all_tasks()
            # Option 8: Exit the program
            else :
                print("Exiting the program...")
                print("Goodbye!")
                break
        # Handle non-integer user input
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
        # Handle unexpected runtime errors
        except Exception as e:
            print("An error occurred:", str(e))

# Call the main function to start the program
main()
