from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input("What would you like? ("+menu.get_items()+")")
    if choice == "off":
        print("Machine turned off! ")
        is_on = False
    if choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)

        if drink is None:
            print("We don't have that drink, choose again!")
        else:
            if not coffee_maker.is_resource_sufficient(drink):
                print("Our resources are insufficient to make that drink :/")
            else:
                if not money_machine.make_payment(drink.cost):
                    print("Money not sufficient to make the drink. Insert More! ")
                else:
                    coffee_maker.make_coffee(drink)

