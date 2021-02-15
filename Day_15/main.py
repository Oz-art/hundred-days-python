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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def ingredients_checker(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


def make_coffee(menu_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {menu_name}, enjoy!!")


def process_coins():
    print("insert coins..")
    total = int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: "))*0.1
    total += int(input("how many nickles?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received>drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry there is not enough money. Money Refunded")
        return False


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on = False
    elif choice=="report":
        print(f"Water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} ml")
        print(profit)
    else:
        drink = MENU[choice]
        if ingredients_checker(drink['ingredients']):
            money = process_coins()
            if is_transaction_successful(money, drink['cost']):
                make_coffee(choice, drink['ingredients'])


