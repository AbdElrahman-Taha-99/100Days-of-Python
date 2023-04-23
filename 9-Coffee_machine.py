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

profit = 0


def check_resources(drink):
    """Checks if the drink can be made using the available resources or not and returns TRUE or FALSE"""
    not_available = False
    if resources['water'] < MENU[drink]['ingredients']['water']:
        print('Sorry, there is not enough water.')
        not_available = True
    if resources['coffee'] < MENU[drink]['ingredients']['coffee']:
        print('Sorry, there is not enough coffee.')
        not_available = True
    if drink != 'espresso' and resources['milk'] < MENU[drink]['ingredients']['milk']:
        print('Sorry, there is not enough milk.')
        not_available = True
    return not_available


def process_coins(drink, payment):
    """Function that checks whether the payment is sufficient or not and returns TRUE or FALSE and returns the change [boolean, change]"""
    all_good = True
    change = 0
    cost = MENU[drink]['cost']
    if payment < cost:
        print("Sorry, that's not enough money. Money refunded.")
        all_good = False
        return all_good, change, 0
    elif payment > cost:
        change = payment - cost
        return all_good, change, cost


def make_coffe(drink):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    if drink != 'espresso':
        resources['milk'] -= MENU[drink]['ingredients']['milk']


working = True
check = True
while working:
    # TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino)
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == 'off':
        working = False
    # TODO: 3. Print report.
    elif choice == 'report' :
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffe: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    # TODO: 4. Check resources sufficient?
    else:
        check = check_resources(choice)
        if not check:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
    # TODO: 5. Process coins.
            total_paid = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
            [check_coins, change, cost] = process_coins(choice, total_paid)
            profit += cost
    # TODO: 6. Check transaction successful?
            if check_coins:
                print(f"Here is ${change} in change.")
    # TODO: 7. Make Coffee.
                make_coffe(choice)
                print(f"Here is your {choice} ☕ Enjoy!")
