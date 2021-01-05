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
    "coffee": 100
}
profit = 0


# TODO: 1 Prompt user
def print_menu():
    for item in MENU:
        print(f"{item} Cost: ${MENU[item]['cost']}")


def take_order():
    """Prompts the user for an order and returns the order. To turn off, input 'off'"""
    print_menu()
    order = input("What would you like?\n")
    if order == 'off':
        turn_off()
    else:
        return order



# TODO: 2 Turn off Coffee Machine by entering "off"
def turn_off():
    global on
    on = False


# TODO 3 Print report showing resource level
def display_report():
    for item in resources:
        if item == 'water' or item == 'milk':
            measure = 'ml'
        else:
            measure = 'g'
        print(f"{item.capitalize()}: {resources[item]}{measure}")
    print(f"Money: ${profit}")
# TODO Check if resources are sufficient
def check_resources(order):
    """Returns True if there are enough resources to produce a given order. Else returns false"""
    for resource in MENU[order]['ingredients']:
        resource_required = MENU[order]['ingredients'][resource]
        resource_level = resources[resource]
        if resource_required > resource_level:
            print(f"Sorry, there is not enough {resource}")
            return False
    return True




# TODO Process coins

def process_coins():
    """Takes in coins and returns the total value"""
    print("Please insert your coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01
    total = quarters * quarter_value + dimes * dime_value + nickels * nickel_value + pennies * penny_value
    return total

# TODO 6 Check if transaction was successful
def check_transaction(order, payment):
    """Checks if the given payment is enough for a given order.
    If it is, then it adds the cost
     of the order to profit and produces the change, and returns True.
     Otherwise, it gives a refund and
     returns False"""
    order_cost = MENU[order]['cost']
    if payment >= order_cost:
        change = payment - order_cost
        print(f"Your {order} is on its way!")
        print(f"Here is your change of ${change}")
        global profit
        profit += order_cost
        return True
    else:
        print(f"Sorry, a {order} costs ${order_cost}. ${payment} is not enough."
              f" Here is a refund of your payment: ${payment}")
        return False

# TODO 7 Make Coffee, Here is your {drink} enjoy!
def make_order(order):
    for resource in MENU[order]['ingredients']:
        resources[resource] -= MENU[order]['ingredients'][resource]

    print(f"Here is your {order}, enjoy!")

#  # , show prompt again
on = True
while on:
    order = take_order()
    enough_resources = check_resources(order)

    if enough_resources:
        payment = process_coins()
        valid_payment = check_transaction(order, payment)
        if valid_payment:
            make_order(order)
