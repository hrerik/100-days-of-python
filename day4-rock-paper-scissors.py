import random

ascii_art = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

user_pick = int(input("ROCK PAPER SCISSORS\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n> "))
computer_pick = random.randint(0,2)

print(f"You chose {ascii_art[user_pick]}")
print(f"The computer chose {ascii_art[computer_pick]}")

if user_pick == computer_pick:
    print("It's a draw")
elif user_pick == computer_pick+1 or (user_pick == 0 and computer_pick == 2): # accounts for all cases the player wins
    print("YOU WON!!!")
else:
    print("YOU LOSE!!!")
