MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "capuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    },

}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resources_sufficient(order_ingredients):
    """verifies if resources are sufficient to make the order."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """returns the total of the coins inserted on the machine."""
    print('Please insert coins.')
    total = int(input("how many quarters? "))* 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print (f"Here is ${change} of change.")
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here's your {drink_name}")

is_on = True

while is_on:
    choice = input("What yould you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        print(f"Water:{resources['water']}ml")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink['ingredients'])


