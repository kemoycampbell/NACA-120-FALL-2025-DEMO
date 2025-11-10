#create a empty dictionary
games = {} #- option 1
#games = dict() # - option 2

#test data
# games = {
#     '123': {'id': '123', 'username': 'nathan', 'kills': 200, 'death': 300, 'matches': 500}, 
#     '444': {'id': '444', 'username': 'ahmed', 'kills': 1000, 'death': 1111, 'matches': 2111}, 
#     '999': {'id': '999', 'username': 'nicartan', 'kills': 500, 'death': 100, 'matches': 600}, 
#     '000': {'id': '000', 'username': 'tanjiro', 'kills': 1000, 'death': 880, 'matches': 1880}
#     }

def menu():
    print("menu options\n===========")
    options = [
        "Add player",
        "Remove player",
        "Show player record",
        "Show all records",
        "Exit"
    ]

    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    
    choice = input("Enter your selection:")
    return choice

def add_player():
    id = input("Enter the player id:")
    username = input("Enter the player username:")
    kills = int(input("Enter the player kills:"))
    death = int(input("Enter the player death:"))
    matches = kills + death

    player_record = {
        "id":id,
        "username":username,
        "kills":kills,
        "death":death,
        "matches":matches

    }

    #print(player_record)
    #add the player dictionary the the game dictionary
    games[id] = player_record
    print(f"Player {player_record} was added")

    #print(games)
def remove_player():
    if len(games) == 0:
        print("No player to remove as the game dictionary is empty")
    else:
        id = input("Enter the player's id to remove:")
        if id in games:
            #del games[id] - option 1
            games.pop(id) # - option 2
            print("The player record was removed")
        else:
            print(f"No match found for {id}")

def show_player_record():
    id = input("Enter the player's id:")
    if id in games.keys():
        print(f"The record for {id}:")
        print(f"{games[id]}")
    else:
        print(f"No match found for {id}")

#menu()
# for i in range(4):
#     add_player()

# print(games)
# #show_player_record()
# remove_player()
# print(games)


# print("show all keys:")
# print(games.keys()) - option 1
# for key in games: - option 2
#     print(key)
# for key in games.keys(): - option 3
#     print(key)

def main():
    while True:
        #show the menu options
        selection = menu()
        #perform the optin based on which menu selected
        if selection == "1":
            add_player()
        elif selection == "2":
            remove_player()
        elif selection == "3":
            show_player_record()
        elif selection == "4":
            if len(games) == 0:
                print("No player data to show")
            else:
                print("Player records\n===========")
                for key in games:
                    print(f"{games[key]}")
        elif selection == "5":
            print("Thank you for using NACA-120 COD")
            print("Goodbye!")
            break
        else:
            print("Invalid selection!")
        
        print("\n")

main()
    


