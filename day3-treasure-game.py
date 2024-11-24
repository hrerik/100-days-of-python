print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print('''Welcome to Treasure Island. 
Your mission is to find the treasure.
''')

path = input("You are in the forest with two path ahead. Which way do you want to go: right or left?\n").lower()

if path == "left":
    river = input("Leaving the forest you find a large river. You can either wait for a boat to come or swim across it. What will you do: wait or swim?\n").lower()
    
    if river == "wait":
        door = input("Crossing the river through a boat, you then find a large house with apparently three different doors. Which one do you pick: blue, red or yellow?\n").lower()
        
        if door == "red":
            print("Upon entering the red door there was a large demon inside that drags you to the confines of hell, where you'll spend eternity. GAME OVER...")
        elif door == "blue":
            print("After entering the house through the blue door you find yourself in the middle of the antartica with no shelter around and you die of hypothermia. GAME OVER...")
        elif door == "yellow":
            print("Inside the house you find the longed treasure you've been looking for. YOU WIN!!!")
        else:
            print("Your answer created a singularity and a black hole, sucking the entire universe into a single point. And you die. GAME OVER...")
    else:
        print("Oh oh, you were attacked by the River Gang Crocodiles and perished. GAME OVER...")
else:
    print("Oh oh, the path you chose made you fall directly in a hole. GAME OVER...")
