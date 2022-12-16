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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources():
    """Checks if resources are available and returns a value"""
    # print(drink['ingredients'])
    for item in resources:
        # print(resources[item])
        if resources[item] >= drink['ingredients'][item]:
            return True

    return False


def insert_coins():
    """Take various coins inserted and returns the total amount"""
    print("Please insert coins")
    dime = int(input("how many dimes : "))
    quarter = int(input("how many quarters: "))
    pennies = int(input("How many pennies: "))
    nickles = int(input("How many nickels: "))
    total_amount = (dime * 0.10) + (quarter * 0.25) + (pennies * 0.01) + (nickles * 0.05)

    return total_amount


def is_transaction_successful(money_received, drink_cost):
    """Returns a value if  money required is enough for user_purchase"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        return f"Here is your {change} in change"
    else:
        return "Sorry that's not enough money. Money refunded."


def make_coffee(choice, order_ingredients):
    "Removes the ingredients used from the ingredient available"
    for item in resources:
        # print(resources[item])
        # print(order_ingredients[item])
        resources[item] -= order_ingredients[item]
        print("Here is your coffee enjoy!")
        return resources


def update_resources():
    update_amount = int(input("Enter resources update amount: "))
    for item in resources:
        # print(item)
        resources[item] += update_amount
    return resources


is_on = True

while is_on:
    choice = input("What would you like to order?(espresso,latte,cappuccino) ?  ").lower().strip()
    if choice == 'off':
        is_on = False
    elif choice == 'update':
        print(update_resources())
    elif choice == 'report':
        print("Water: 100ml")
        print("Milk: 50 ml")
        print("Coffee: 76g")
        print("Money: $2.5")
    else:
        drink = MENU[choice]
        if check_resources():
            payment = insert_coins()
            # print(payment)
            print(is_transaction_successful(payment, drink['cost']))
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
