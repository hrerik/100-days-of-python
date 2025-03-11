import random

logo = """
  _   _                 _                _____                     _             
 | \ | |               | |              / ____|                   (_)            
 |  \| |_   _ _ __ ___ | |__   ___ _ __| |  __ _   _  ___  ___ ___ _ _ __   __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
 | |\  | |_| | | | | | | |_) |  __/ |  | |__| | |_| |  __/\__ \__ \ | | | | (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                                                            __/ |
                                                                           |___/ 
"""

def get_number(n):
    """Will keep asking user for number until a valid answer is given"""
    try:
        return int(n)
    except ValueError:
        new_ans = input("Your guess must be a number!!\n>")
        return get_number(new_ans)

while True:
    print(logo)
    print("Welcome to number guessing game.")
    ans = input("In which difficulty do you want to play in? Easy (e) or hard (h)?\n>")

    while ans not in ["e","h"]:
        ans = input("Invalid answer!\n>")

    if ans == "e":
        lives = 10
    else:
        lives = 5
    print(f"You have {lives} lives.")

    number = random.randint(1,100)
    print("Guess a number from 1 to 100...")
    guess_num = get_number(input(">"))

    while guess_num != number:
        if guess_num > number:
            print("Too high ")
        else:
            print("Too low")

        lives -= 1
        if lives > 0:
            print(f"You have {lives} lives.")
            guess_num = get_number(input(">"))
        else:
            print("You ran out of lives!! :(")
            break
    else:
        print("You got it right!!!")

    replay = input("Do you want to play again? (y/n)\n>")
    while replay not in ["y","n"]:
        replay = input("Invalid answer!\n>")
    if replay == "n":
        break