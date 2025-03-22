from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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


coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

print(logo)
while True:
    ans = input(f"What would you like? ({menu.get_items()}): ")
    drink = menu.find_drink(ans)
    if ans == "off":
        print(goodbye)
        break
    elif ans == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif drink is not None:
        if coffeeMaker.is_resource_sufficient(drink):
            print(f"The {ans} will cost ${drink.cost}.")
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
        else:
            print(f"Sorry, there are insufficient resources for a {ans}")
    else:
        print("Invalid response :(")

    print(logo)
