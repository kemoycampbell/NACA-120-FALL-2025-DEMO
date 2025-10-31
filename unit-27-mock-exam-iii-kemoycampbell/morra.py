"""
@author: Kemoy Campbell
date: 10/31/2025
Project code name: HandBattle
Purpose:
    A program that plays Morra
"""

import datetime
import random

# PREDEFINED BELOW, DO NOT MODIFY ANY CODE
LINE_SEPARATOR = "=============================="
HAND_MIN = 1
HAND_MAX = 3

"""
    This function will print the header containing 
    the game name, version number, and today's date and time
"""


def get_game_header():
    now = datetime.datetime.now()

    return \
        f"{LINE_SEPARATOR}" \
        "\nMorra" \
        "\n\tGame Version 1.0" \
        f"\n{LINE_SEPARATOR}" \
        f"\nDate and Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"


"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        game_round: The current round in the game

    returns the xp for the round
"""


def generate_xp(game_round):
    if game_round < 1:
        game_round = 1

    return random.randint(HAND_MIN, HAND_MAX) * game_round


"""
    This function will randomly pick a hand for the computer.
    This will return a hand from HAND_MIN (1) to HAND_MAX (3)
"""


def get_computer_hand():
    return random.randint(HAND_MIN, HAND_MAX)


"""
    This function will return a random hand sum guess for the computer.
    This will return a hand sum from HAND_MIN * 2 + HAND_MIN * 2
"""


def get_computer_guess():
    return random.randint(HAND_MIN, HAND_MAX) + random.randint(HAND_MIN, HAND_MAX)
# PREDEFINED ABOVE, DO NOT MODIFY ANY CODE


# STUDENT CODE HERE
def determine_winner(player_hand, player_guess, computer_hand, computer_guess):
    #combine both hand sum
    hand_sum = player_hand + computer_hand

    #check to see if we have a tie
    if player_guess == computer_guess and player_guess == hand_sum:
        return "tie"

    #check if player guess match the hand sum
    #if the player guess right then the player is the winner
    if player_guess == hand_sum:
        return "player"
    #if the computer guess right then the computer is the winner
    elif computer_guess == hand_sum:
        return "computer"
    # else:
    #     return "no winner"
    #other option
    return "no winner"

def get_player_hand():
    while True:
        try:
            #ask for number
            hand = input("Please enter a number between "+ str(HAND_MIN)+"-"+str(HAND_MAX)+":")
            #convert hand to int
            hand = int(hand)

            #validate to make sure in right range
            if hand < HAND_MIN or hand > HAND_MAX:
                print("Please enter 1-3")
                continue
                #raise ValueError("Please enter 1-3")
            return hand
        except:
            print("Error!Please enter a number between "+ str(HAND_MIN)+"-"+str(HAND_MAX))
def get_player_guess():
    while True:
        try:
            #ask for number
            guess = input("Please guess a number between "+ str(HAND_MIN * 2)+"-"+str(HAND_MAX * 2)+":")
            #convert guess to int
            guess = int(guess)

            #validate to make sure in right range
            if guess < HAND_MIN * 2 or guess > HAND_MAX * 2:
                print("Please guess 2-6")
                continue
                #raise ValueError("Please enter 2-6")
            return guess
        except:
            print("Error!Please guess a number between "+ str(HAND_MIN * 2)+"-"+str(HAND_MAX * 2))

    
def get_stats(player_score, player_wins, computer_score, computer_wins):
    stats = "Game stats\n=========\n"
    stats+="Player Score:"+str(player_score)
    stats+="\nPlayer wins:" + str(player_wins)
    stats+="\nComputer Score:"+str(computer_score)
    stats+="\nComputer wins:" + str(computer_wins)
    return stats


def get_play_again_prompt():
    while True:
        play_again = input("Do you want to play again (yes or quit):")
        if play_again=='yes' or play_again=='quit':
            return play_again
        print("Please type yes or no!")





def main():
    player_score = 0
    player_wins = 0
    computer_score = 0
    computer_wins = 0
    game_round = 1

    # STUDENT CODE HERE
    # ...

    #code testing
    #remove later
    # player_hand = 1
    # computer_hand = 2
    # computer_guess = 4
    # player_guess  = 4
    # winner = determine_winner(player_hand,player_guess,computer_hand, computer_guess)
    # print(winner)

    # player_hand = get_player_hand()
    # print(player_hand)

    # player_guess = get_player_guess()
    # print(player_guess)

    #game stats
    # player_score= 1
    # player_wins =1
    # computer_score = 1
    # computer_wins = 1
    # stats = get_stats(player_score, player_wins, computer_score, computer_wins)
    # print(stats)

    # #play again
    # again = get_play_again_prompt()
    #print(again)
    header = get_game_header()
    print(header)

    #during each rounds
    while True:
        #show stats after round 1
        if game_round > 1:
            print(get_stats(player_score, player_wins, computer_score, computer_wins))
    
        #show current round
        print("Round", game_round)

        #get computer hand
        computer_hand = get_computer_hand()
        computer_guess = get_computer_guess()
        player_hand = get_player_hand()
        player_guess = get_player_guess()


        winner = determine_winner(player_hand,player_guess,computer_hand,computer_guess)

        #give scores and points to right winner
        if winner == "computer":
            computer_wins+=1
            computer_score+=generate_xp(game_round)
        elif winner == "player":
            player_wins+=1
            player_score+=generate_xp(game_round)

        #show what the computer pick and the results
        print("Computer's hand", computer_hand)
        print("Computer's guess", computer_guess)

        print("The sum of both hands is", computer_hand+ player_hand)
        print("The winner is", winner)

        #ask the user if they want to play again
        play_again = get_play_again_prompt()
        if play_again == 'quit':
            break
        
        #increase the game round by 1 if the user want to play again
        game_round+=1

    print("Thank you for playing Morra!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram was ended abruptly by the user\n")
