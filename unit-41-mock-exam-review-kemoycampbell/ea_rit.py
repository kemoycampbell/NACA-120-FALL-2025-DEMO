import re  # Import the regular expressions module for pattern matching

# Predefined variables
games_records = [] #this will keep a list of all game sales

# Predefined function
def display_menu():
    print("Menu Options:")
    print("1. Create a new sale")
    print("2. Remove a record")
    print("3. Show all sales")
    print("4. Filter sale by platform")
    print("5. Exit")
    
# Predefined function
def menu_selection():
    display_menu()  # Show the menu to the user
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))  # Ask user for a number input
            if choice < 1 or choice > 5:  # Validate input is between 1 and 5
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue  # If invalid, loop back to ask again
            
            return choice  # Valid choice, return it
                
        except ValueError:  # Handle case where input is not an integer
            print("Invalid input. Please enter a valid number.")
            
# functions to be completed by the student goes here
"""
This function will use regex to ensure that the date is in the format MM-DD-YYYY.
If the date is in the format specified above, return True otherwise return False. 
"""
def is_valid_date(date):
    pattern = r'\d{2}-\d{2}-\d{4}'  # Regex pattern: 2 digits-2 digits-4 digits
    result = re.match(pattern, date)  # Check if the date matches the pattern
    if result == None:  # No match found
        return False
    return True  # Match found, date is valid

def create_sale():
    name = input("Enter the game name:")  # Prompt user for game name
    platform = input("Enter the game platform:")  # Prompt user for platform
    #validate the date
    while True:
        date = input("Enter the game date of sale:")  # Ask user for date
        ####################
        # option 1
        #####################
        #if the date is fine then we dont need to ask the user again
        #we just break out of the loop
        # if is_valid_date(date)==True:
        #     break
        # #the date is not valid so ask again
        # #show user error message
        # print("Invalid date. Please enter the date in the format:MM-DD-YYYY")

        #############################
        # OPTION 2
        ############################
        #the date is not valid
        if is_valid_date(date) == False:
            #show error message
            print("Invalid date. Please enter the date in the format:MM-DD-YYYY")
            continue #go back to loop
        #everything is fine, break out of the loop
        break

    cost = input("Enter the game cost:")  # Ask user for cost of game

    #create the game record in form of dictionary
    game = {"name":name, "platform":platform, "date":date, "cost":cost}
    #add the game record to the list
    games_records.append(game)
    print(f"{game} was successfully added to the record")  # Confirm addition to user

def remove_record():
    #prompt the user for the name and platform of the game sale record to remove from the list
    name = input("Enter the name of the game to remove:")
    platform = input("Enter the name of the platform to remove:")

    #we first assume no match is found
    match_result = False
    #loop through the record and search for the match
    for record in games_records:
        #we found the matching name and platform
        if record["name"] == name and record["platform"] == platform:  # Corrected condition
            games_records.remove(record)  # Remove the record from the list
            match_result = True
            #let the user know the record was successfully remove
            print(f"{record} was successfully removed")
            break  # Stop searching after first match
    
    #check if there were no match
    if match_result == False:
        print(f"No match was found for name:{name} and platform:{platform}")  # Notify user

def show_sales():
    #list is empty
    if len(games_records) == 0:
        print("The list is currently empty.")  # Notify user list is empty
    else:
        print("Game sale records:\n========================")
        for record in games_records:
            print(record)  # Print each record in the list

def filter_by_platform_rec(record_list,target,filtered_list):
    #set up the base case.. if the list is empty then we return the filtered list
    if len(record_list) == 0:
        return filtered_list
    
    #search if match and add to filter list
    record = record_list[0]  # Look at first record
    if record["platform"] == target:  # Check if platform matches
        filtered_list.append(record)  # Add matching record to filtered list
    
    #recursive step
    record_list = record_list[1:] #slice the record list and focus on index 1 disregard 0

    #recursively search for match
    return filter_by_platform_rec(record_list, target, filtered_list)  # Recursive call

def filter_by_platform():
    platform = input("Enter the platform to filter by:")  # Ask user which platform to filter
    #the filtered list is initially empty, we have not get any match yet
    filtered_list = []
    matches = filter_by_platform_rec(games_records, platform, filtered_list)  # Get filtered records
    if len(matches) == 0:
        print(f"No matches found for {platform}")  # Notify if no matches
    else:
        print("Matches:")
        for record in matches:
            print(record)  # Print each matching record

def main():
    while True:
        try:
            selection = menu_selection()  # Ask user for menu choice
            if selection == 1:
                create_sale()  # Add a new sale
            elif selection == 2:
                remove_record()  # Remove a record
            elif selection == 3:
                show_sales()  # Show all sales
            elif selection == 4:
                filter_by_platform()  # Filter sales by platform
            elif selection == 5:
                print("Thank you for using EA game sales")  # Exit message
                break  # Exit program
            else:
                print("Invalid selection! select 1-5")  # Extra safety
        except:
            print("Invalid action!")  # Catch any unexpected errors
    
if __name__ == "__main__":
    # Example testing code is commented out
    # date = "12-12-2024"
    # print(is_valid_date(date))
    # date = "12-YA-Cool"
    # print(is_valid_date(date))
    #create_sale()
    # create_sale()
    # remove_record()
    #show_sales()
    # print("Matching records")
    # print(filter_by_platform_rec(games_records, "XBOX",[]))
    #filter_by_platform()
    main()  # Start the main program
