from time import sleep


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 10,
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
    "water": 500,
    "milk": 500,
    "coffee": 500,
}


def validate_input(beverage) -> bool:
    if beverage not in ["cappuccino", "latte", "expresso"]:
        print(f"{beverage}: Invalid input. Check it is spelled correctly and there are no trailing spaces at the "
              f"front/back.")
        return False

    return True


def refill(resource):
    for ingredient in resources:
        if ingredient == resource:
            resources[ingredient] = 500


def print_refill_needed(resource):
    print(f"Not enough {resource} in the maker.")
    order_further = input("Would you like to refill? (Y/N): ")

    if order_further == 'Y':
        refill(resource)
        print(f"Refilling {resource}...please wait")
        sleep(2)
        print("Refill Done!")
    else:
        print("Have a nice day!")
        exit(0)


def enough_resources(beverage):
    bev_ingredients = (MENU.get(beverage)).get("ingredients")

    if bev_ingredients["water"] > resources["water"]:
        print_refill_needed("water")

    if bev_ingredients["milk"] > resources["milk"]:
        print_refill_needed("milk")

    if bev_ingredients["coffee"] > resources["coffee"]:
        print_refill_needed("coffee")


def get_change(total, cost):
    if total >= cost:
        print(f"Your change is ${total-cost}")


def make_beverage(beverage):
    for item in MENU:
        if item == beverage:
            resources["water"] -= MENU.get(item).get("ingredients").get("water")
            resources["coffee"] -= MENU.get(item).get("ingredients").get("coffee")
            if item != "espresso":
                resources["milk"] -= MENU.get(item).get("ingredients").get("milk")
            break
    print(f"Here is your {beverage} ☕. Enjoy!")


def main():

    while True:
        beverage = (input("What would you like? (cappuccino/latte/expresso): ")).lower()
        if validate_input(beverage) is not True:
            continue
        enough_resources(beverage)
        cost = (MENU.get(beverage)).get('cost')
        print(f"The cost of a {beverage} is ${cost}")
        print("Please insert coins now.")
        quarters = float(input("How many quarters: "))
        loonies = float(input("How many loonies: "))
        toonies = float(input("How many toonies: "))
        total = quarters*0.25 + loonies*1.0 + toonies*2.0
        get_change(total, cost)
        sleep(1)
        make_beverage(beverage)
        order_further = input("Would you like another drink? (Y/N): ")
        if order_further == "Y":
            continue
        else:
            print("Have a nice day!")
            break


if __name__ == "__main__":
    main()
