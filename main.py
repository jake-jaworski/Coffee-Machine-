from menu import MENU, resources


def calculate_payment():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    funds = quarters + dimes + nickels + pennies
    return funds


def transaction_successful(money, cost, product):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Your change is ${change}")
        return True
    else:
        print(f"Sorry, ${money} was not enough for the {product}. Your funds have been returned. Please try again.")
        return False


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        return True


def make_drink(product, ingredients):
    print(f"Here is your {product}!")
    for item in ingredients:
        resources[item] -= ingredients[item]


machine_on = True


while machine_on:
    drink_choice = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()

    if drink_choice == "off":
        machine_on = False
    elif drink_choice == "report":
        print(f"Water remaining: {resources['water']} units")
        print(f"Milk remaining: {resources['milk']} units")
        print(f"Coffee remaining: {resources['coffee']} units")
    else:
        drink = MENU[drink_choice]
        if check_resources(ingredients=drink["ingredients"]):
            payment = calculate_payment()
            if transaction_successful(money=payment, cost=drink["cost"], product=drink_choice):
                make_drink(product=drink_choice, ingredients=drink["ingredients"])







