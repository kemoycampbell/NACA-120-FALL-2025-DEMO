"""
@author: <Your name>
date: <today's date>
Project code name: HandBattle
Purpose:
    A program that play rock, paper, scissors
"""

import datetime
import random

#PREDEFINED
"""
    This function will print the header containing 
    Rock, paper,scissors as well as today's date and time
"""
def game_header():
    print("==============================")
    rock = "Rock:🗿"
    paper = "Paper:📃"
    scissors = "Scissors:✂️"
    print(f"{rock} {paper} {scissors}")
    print("\n\tGame Version 0.1")
    print("==============================\n")
    now = datetime.datetime.now()
    print("Date and Time:",now.strftime("%d/%m/%Y %H:%M:%S"))

#PREDEFINED
"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        round: The current round in the game

    returns the xp for the round
"""
def generate_xp(round):
    min_xp = 1
    max_xp = 30
    xp = random.randint(min_xp, max_xp)
    return xp * round

#PREDEFINED
"""
    This function will randomly pick a choice for the computer.
    This will return one of the following, "rock", "paper" or "scissor"
"""
def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)


#STUDENT CODE HERE
#STUDENT FUNCTIONS HERE
def determine_winner(player_choice, computer_choice):
    #check for tie
    if player_choice == computer_choice:
        return "It's a tie!"
    
    #check if player beats computer
    if player_choice == "rock" and computer_choice == "scissor":
        return "Player wins!"
    
    elif player_choice == "paper" and computer_choice == "rock":
        return "Player wins!"
    
    elif player_choice == "scissor" and computer_choice == "paper":
        return "Player wins!"
    
    return "Computer wins!"

def get_user_choice():
    while True:
        try:
            choice = input("Enter your choice(rock,paper or scissor):")
            if choice == "rock" or choice =="paper" or choice =="scissor":
                return choice
            print("Invalid choice, you must pick rock or paper or scissor")
        except:
            print("Invalid choice, you must pick rock or paper or scissor")
    pass



#PREDEFINED
def main():
    #STUDENT CODE HERE - VARIABLES DECLARATION
    game_round = 1
    computer_choice = "N/A"
    user_choice = "N/A"
    winner = "N/A"
    total_computer_score = 0
    total_player_score = 0
    total_computer_xp = 0
    total_player_xp = 0
    game_header()
    while True:
        #STUDENT CODE HERE
        try:
            print("Round", game_round)
            print("Game Stats\n===========")
            print("Previous computer choice", computer_choice)
            print("Previous player choice", user_choice)
            print("Previous winner", winner)
            print("Total comptuer score", total_computer_score)
            print("Total computer xp", total_computer_xp)
            print("Total player score", total_player_score)
            print("Total computer xp", total_player_xp)

            computer_choice = get_computer_choice()
            user_choice = get_user_choice()
            #main #5
            print("You pick:"+ user_choice +" and Computer:"+ computer_choice)
            winner = determine_winner(user_choice, computer_choice)
            print("Winner", winner)

            if winner == "Player wins!":
                total_player_score+=1
                total_player_xp = generate_xp(game_round)
            elif winner == "Computer wins!":
                total_computer_score+=1
                total_computer_xp = generate_xp(game_round)
            
            play_again = input("Do you want to play again(yes/quit):")
            if play_again == "quit":
                print("Thank you for playing")
                break
            
            #increase the round if the user want to continue the game
            game_round+=1
        except:
            print("An error occurred.. Game resume")



#PREDEFINED
main()
