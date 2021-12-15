from data import MENU, resources


# print(MENU["espresso"]["ingredients"]["coffee"])
def update_resources(drink, resource):
    water_left = resource["water"] - MENU[drink]["ingredients"]["water"]
    milk_left = resource["milk"] - MENU[drink]["ingredients"]["milk"]
    coffee_left = resource["coffee"] - MENU[drink]["ingredients"]["coffee"]
    resource["money"] += MENU[drink]["cost"]
    return {"water": water_left, "milk": milk_left, "coffee": coffee_left, "money": resource["money"]}


def check_resources(drink, resource):
    water_check = resource["water"] - MENU[drink]["ingredients"]["water"]
    milk_check = resource["milk"] - MENU[drink]["ingredients"]["milk"]
    coffee_check = resource["coffee"] - MENU[drink]["ingredients"]["coffee"]
    if water_check >= 0 and milk_check >= 0 and coffee_check >= 0:
        return True
    else:
        if water_check<0:
            print("Not enough Water")
        elif milk_check<0:
            print("Not enough Milk")
        else:
            print("Not enough coffee")
        return False


def coins_inserted():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_transaction(coin, drink):
    change = round(coin - MENU[drink]["cost"], 2)
    if change >= 0:
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕. Enjoy!")
        return True
    else:
        print("Not enough money for the transaction. Money refunded!")
        return False


def report(resource):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    money = resource["money"]
    print(f"Water left: {water}ml")
    print(f"Milk left: {milk}ml")
    print(f"Coffee left: {coffee}g")
    print(f"Money in the machine: ${money}")


# TODO: I need a way to update resources
# TODO: I need a way to check if the resources are sufficient
# TODO: I need a way to check if the transaction is successful

machine_ON = True
# prompting user: while machine is ON
while machine_ON:
    user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_drink == 'report':
        report(resources)
    elif user_drink == 'off':
        machine_ON = False
    elif check_resources(user_drink, resources):
        coins = coins_inserted()
        if check_transaction(coins, user_drink):
            resources = update_resources(user_drink, resources)


