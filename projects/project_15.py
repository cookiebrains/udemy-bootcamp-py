MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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
}

money = float(0)


def get_money():
    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?:"))
    pennies = float(input("How many pennies?:"))
    total_collected = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total_collected


def get_change(drink, total_collected):
    global money
    if total_collected > MENU[drink]["cost"]:
        money += MENU[drink]["cost"]
        change = (total_collected - MENU[drink]["cost"])
        change = "{:.2f}".format(change)
        print(f"Here is ${change} in change.")
    elif total_collected == MENU[drink]["cost"]:
        money += MENU[drink]["cost"]
        print("Thank you. You have inserted the exact cost of your drink.")


def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True


def use_resources(drink):
    global resources
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    return True


def report():
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money:.2f}")


def order(drink):
    # check resources
    # if enough resources, use resources and ask for money, wait UP, only uses resources if we get enough money.
    use_resources(drink)


def machine_on():
    while True:
        drink = input("What would you like to order? (espresso/latte/cappuccino):")
        if drink == "espresso" or drink == "latte" or drink == "cappuccino":
            if check_resources(drink):
                customer_paid = get_money()
                if customer_paid >= MENU[drink]["cost"]:
                    use_resources(drink)
                    get_change(drink, customer_paid)
                    print(f"Here is your {drink}. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                continue
        elif drink == 'report':
            report()
        elif drink == "off":
            break


def run():
    machine_on()
    print("Machine is now off.")
    report()

