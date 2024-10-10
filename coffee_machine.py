import Menu
from Menu import MENU, resources

def defining_money():
    penny = input("How many penny?: ")
    penny = float(penny) * 0.01
    dime = input("How many dime?: ")
    dime = float(dime) * 0.10
    nickel = input("How many nickel?: ")
    nickel = float(nickel) * 0.05
    quarter = input("How many quarter?: ")
    quarter = float(quarter) * 0.25
    change = penny + dime + nickel + quarter
    return round(change,2)

change = 0

stop = 0
while stop == 0:
    your_deserve = input("What would you like (espresso/latte/cappuccino): ").lower()
    
    if your_deserve == "report":
        
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffe: {resources["coffee"]}")
        print(f"Money: {change}")
    # First option
    elif your_deserve == "espresso":
        change = defining_money()

        if change > MENU[your_deserve]["cost"] :
    
            if resources["water"] >= MENU[your_deserve]["ingredients"]["water"] and resources["coffee"] >= MENU[your_deserve]["ingredients"]["coffee"]:

                change = change - MENU[your_deserve]["cost"]
                print(f"Here is your {your_deserve}, enjoy!")
                print(f"Your change is {change}")

                resources["water"] = resources["water"] - MENU[your_deserve]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[your_deserve]["ingredients"]["coffee"]

            else:
                print("Sorry this machine doesn't have enough ingredients. :(")

        else:
            print("You don't have enough money, sorry")

    elif your_deserve == "latte":
        change = defining_money()
        if change > MENU[your_deserve]["cost"]:
            if resources["water"] >= MENU[your_deserve]["ingredients"]["water"] and resources["coffee"] >= MENU[your_deserve]["ingredients"]["coffee"] and resources["milk"] >= MENU[your_deserve]["ingredients"]["milk"]:
                change = change - MENU[your_deserve]["cost"]
                print(f"Here is your {your_deserve}, enjoy!")
                print(f"Your change is {change}")

                resources["water"] = resources["water"] - MENU[your_deserve]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[your_deserve]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[your_deserve]["ingredients"]["coffee"]

            else:
                print("Sorry this machine doesn't have enough ingredients. :(")
                stop = 1

        else:
            print("You don't have enough money, sorry")
            stop = 1

    elif your_deserve == "cappuccino":
        change = defining_money()
        if change > MENU[your_deserve]["cost"]:
            if resources["water"] >= MENU[your_deserve]["ingredients"]["water"] and resources["coffee"] >= MENU[your_deserve]["ingredients"]["coffee"] and resources["milk"] >= MENU[your_deserve]["ingredients"]["milk"]:
                change = change - MENU[your_deserve]["cost"]
                print(f"Here is your {your_deserve}, enjoy!")
                print(f"Your change is {change}")

                resources["water"] = resources["water"] - MENU[your_deserve]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[your_deserve]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[your_deserve]["ingredients"]["coffee"]

            else:
                print("Sorry this machine doesn't have enough ingredients. :(")
                stop = 1

        else:
            print("You don't have enough money, sorry")
            stop = 1

    elif your_deserve == "off":
        print("The coffee machine is off")
        stop = 1
    else:
        print("You need to select a least one option of these above type of coffe... ")
        stop = 1