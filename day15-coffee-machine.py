MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "coins": 0.0
}

logo = r"""
      ___           ___           ___         ___         ___           ___     
     /  /\         /  /\         /  /\       /  /\       /  /\         /  /\    
    /  /:/        /  /::\       /  /:/_     /  /:/_     /  /:/_       /  /:/_   
   /  /:/        /  /:/\:\     /  /:/ /\   /  /:/ /\   /  /:/ /\     /  /:/ /\  
  /  /:/  ___   /  /:/  \:\   /  /:/ /:/  /  /:/ /:/  /  /:/ /:/_   /  /:/ /:/_ 
 /__/:/  /  /\ /__/:/ \__\:\ /__/:/ /:/  /__/:/ /:/  /__/:/ /:/ /\ /__/:/ /:/ /\
 \  \:\ /  /:/ \  \:\ /  /:/ \  \:\/:/   \  \:\/:/   \  \:\/:/ /:/ \  \:\/:/ /:/
  \  \:\  /:/   \  \:\  /:/   \  \::/     \  \::/     \  \::/ /:/   \  \::/ /:/ 
   \  \:\/:/     \  \:\/:/     \  \:\      \  \:\      \  \:\/:/     \  \:\/:/  
    \  \::/       \  \::/       \  \:\      \  \:\      \  \::/       \  \::/   
     \__\/         \__\/         \__\/       \__\/       \__\/         \__\/    
"""

goodbye = r"""
      ___           ___           ___                                                   ___     
     /\__\         /\  \         /\  \         _____         _____                     /\__\    
    /:/ _/_       /::\  \       /::\  \       /::\  \       /::\  \         ___       /:/ _/_   
   /:/ /\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \       /|  |     /:/ /\__\  
  /:/ /::\  \   /:/  \:\  \   /:/  \:\  \   /:/  \:\__\   /:/ /::\__\     |:|  |    /:/ /:/ _/_ 
 /:/__\/\:\__\ /:/__/ \:\__\ /:/__/ \:\__\ /:/__/ \:|__| /:/_/:/\:|__|    |:|  |   /:/_/:/ /\__\
 \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  /  __|:|__|   \:\/:/ /:/  /
  \:\  /:/  /   \:\  /:/  /   \:\  /:/  /   \:\  /:/  /   \::/_/:/  /  /::::\  \    \::/_/:/  / 
   \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /   ~~~~\:\  \    \:\/:/  /  
    \::/  /       \::/  /       \::/  /       \::/  /       \::/  /         \:\__\    \::/  /   
     \/__/         \/__/         \/__/         \/__/         \/__/           \/__/     \/__/    """
# (r) on (r""") to denote raw string (look up docs)

def sufficient_resources(option):
    menu = MENU[option]["ingredients"]
    for ingredient in menu:
        if resources[ingredient] < menu[ingredient]: return False
    return True

def validate_coins(coins):
    try:
        return int(coins)
    except ValueError:
        coins = input("Insert a valid numerical amount, please.\n>")
        return validate_coins(coins)
    
def make_drink(drink):
    global resources
    ingredients = MENU[drink]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here's your {drink}. Enjoy!!")

print(logo)
while True:
    ans = input("What would you like? (espresso/latte/cappuccino): ")
    if ans == "off":
        print(goodbye)
        break
    elif ans == "report":
        print("Resources:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Coins: ${resources['coins']}")
    elif ans in MENU:
        if sufficient_resources(ans):
            print(f"The {ans} will cost ${MENU[ans]['cost']}. Insert your coins:")
            quarters = validate_coins(input("Quarters ($0.25) = "))
            dimes = validate_coins(input("Dimes ($0.10) = "))
            nickels = validate_coins(input("Nickels ($0.05) = "))
            pennies = validate_coins(input("Pennies ($0.01) = "))
            amount = round(quarters / 4 + dimes / 10 + nickels / 20 + pennies / 100, 2)
            cost = MENU[ans]['cost']
            if amount >= cost:
                make_drink(ans)
                resources['coins'] += cost
                if amount > cost:
                    change = round(amount - cost, 2)
                    print(f"Your change: ${change}")
            else:
                print("Sorry, you put insufficient cash...")
                print(f"Your change: ${amount}")
        else:
            print(f"Sorry, there are insufficient resources for a {ans}")
    else:
        print("Invalid response :(")

    print("\n"*6)
    print(logo)
