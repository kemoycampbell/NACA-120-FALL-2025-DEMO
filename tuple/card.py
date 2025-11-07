import random
def card_info(card):
    return f"Rank:{card[0]}\nSuit:{card[1]}\nColor:{card[2]}\n\n"

# card1 = ("A","Heart","Red")
# card2 = ("A","Spade","Black")

# print(f"card 1 info:{card_info(card1)}")
# print(f"card 2 info:{card_info(card2)}")

# #storing tuples with list
# cards = [card1, card2]

# print("The card lists:")
# for card in cards:
#     print(card)

def shuffle(cards):
    #https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    # -- To shuffle an array a of n elements (indices 0..n − 1):
    # for i from n − 1 down to 1 do
    #     j ← random integer such that 0 ≤ j ≤ i
    #     exchange a[j] and a[i]

    n =  len(cards) - 1
    for i in range(n,0,-1):
      
        j = random.randint(0,i)
        temp = cards[i]
        cards[i] = cards[j]
        cards[j] = temp
    
    return cards


#make 52 cards
print("Making 52 cards")
suits = ["Heart", "Diamond", "Spade", "Club"]
cards = [] # a empty card list to store all cards
for rank in range(2,15):
    #handle for face cards
    if rank == 11:
        rank = "J"
    elif rank == 12:
        rank = "Q"
    elif rank == 13:
        rank = "K"
    elif rank == 14:
        rank = "A"
    
    #each card have 4 suits
    for suit in suits:
        color = "Red"
        if suit == "Spade" or suit == "Club":
            color = "Black"
        # print(f"Rank-{rank}, suit-{suit}, color-{color}")
        card = (rank,suit,color) #create the card tuple
        #add to the list of cards
        cards.append(card)
print("Card generating completed\n")

print(f"Total cards:{len(cards)}")
print("Shuffling the cards")
for i in range(4):
    cards = shuffle(cards)

print("Showing the shuffled cards")
for card in cards:
    print(card)
    
