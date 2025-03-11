# THINGS TO IMPROVE:
# 1. variable naming
# 2. unnecessary usage of dictionaries (code hard to read)
# 3. user experience isn't as good, printed messages could have been shown in a different order

# 'deck' is the initial deck of cards, 'cards' are whose which were picked during the game

import random

deck = ["ACE",2,3,4,5,6,7,8,9,10,10,10,10]
score = {
    "player": 0,
    "computer": 0
}

def get_card():
    return deck[random.randint(0,12)]

def ace_card():
    print("You got an ace!")
    ace = int(input("How much will it value? (11 or 1)\n>"))
    while ace not in [1,11]:
        ace = int(input("Card value invalid.\n>"))
    return ace

def ace_card_pc(pc_cards):
    if sum(pc_cards) <= 10:
        return 1
    else:
        return 11

while True:
    drawing = True
    cards = {"computer": [get_card()]}

    print("################# BLACKJACK #################")
    print(f"Score: {score["player"]}x{score["computer"]}\n") # > Score: 0x0

    print(f"Computer has {cards["computer"][0]}")

    if cards["computer"][0] == "ACE":
        cards["computer"][0] = 11

    while sum(cards["computer"]) < 17 or len(cards["computer"]) == 1:
        cards["computer"].append(get_card())
        cards["computer"][len(cards["computer"])-1] = ace_card_pc(cards["computer"])


    cards["player"] = [get_card(),get_card()]

    print(f"You have {cards["player"][0]} and {cards["player"][1]}.")

    if cards["player"][0] == "ACE":
        cards["player"][0] = ace_card()
    if cards["player"][1] == "ACE":
        cards["player"][1] = ace_card()

    # print(cards["player"])

    while drawing and sum(cards["player"]) < 21:
        ans = input(f"You have {sum(cards["player"])} points, do you want to draw another card? (\"y\"/\"n\")\n>")
        if ans == "y":
            cards["player"].append(get_card())
            if cards["player"][len(cards["player"])-1] == "ACE":
                cards["player"][len(cards["player"]) - 1] = ace_card()
        elif ans == "n":
            drawing = False

    print("The computer got the cards:")
    for card in cards["computer"]:
        print(f"- {card}")

    points_player = sum(cards["player"])
    points_pc = sum(cards["computer"])
    print(f"You have {points_player} points.")
    print(f"The computer has {points_pc} points.")


    if points_player == points_pc:
        print("It's a draw!! Neither scores.")
    elif points_player == 21 or points_pc > 21 or (points_pc < points_player < 21 and points_pc < 21):
        print("The player wins!!")
        score["player"] += 1
    elif points_pc == 21 or points_player > 21 or (points_player < points_pc < 21 and points_player < 21):
        print("The computer wins!!")
        score["computer"] += 1
