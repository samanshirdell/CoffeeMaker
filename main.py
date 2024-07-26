from info import resources, MENU
from replit import clear
profit = 0

def transaction_successful(money_drink, drink_cost):
    global profit
    if money_drink > drink_cost:
        change = round(money_drink - drink_cost, 2)
        print(f"Here is {change} change.")
        profit += change
        return True
    else:
        print("Sorry, That is not enough money. Money refunded...")
        return False


def sufficent_resouce(order_ingredients):
    is_enough = True
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry, That is not enough water. {items}")
            is_enough = False
        return is_enough


def process():
    print("Please insert you coin: ")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    user_choice = input("What would you like: (Expresso/ Latte/ Cappuccino): ").lower()
    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: {profit}")

    elif user_choice == "off":
        clear()
        is_on = False
        print("Thank you for try this..")

    else:
        drink = MENU[user_choice]
        if sufficent_resouce(drink["ingredients"]):
            payment = process()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])