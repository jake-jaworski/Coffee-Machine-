from menu_oop import Menu, MenuItem
from coffee_maker_oop import CoffeeMaker
from money_machine_oop import MoneyMachine

machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while machine_on:
    options = menu.get_items()
    drink = input(f"What would you like to drink? ({options}): ").lower()

    if drink == "off":
        machine_on = False
    elif drink == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


