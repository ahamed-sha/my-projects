

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
# TODO: 8. Add money to the report
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


should_work = True
while should_work:
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    # TODO: 1. Print report of what resources has left
    if choice == "report":
        for k, v in resources.items():
            print(k, v)
            continue

    # TODO: 7. "off" switch
    elif choice == "off":
        should_work = False
        break

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":

        # TODO: 2. What would you like?
        drink = MENU[choice]
        cost_per_drink = drink["cost"]
        ing = drink["ingredients"]
        water_required = ing["water"]
        milk_required = ing["milk"]
        coffee_required = ing["coffee"]

        # TODO: 6. Make coffee
        def make_coffee():
            global resources
            resources["water"] -= water_required
            resources["milk"] -= milk_required
            resources["coffee"] -= coffee_required
            print(f"here is your {choice}, enjoy!")

        # TODO: 4. Process coins by prompting user
        def process_coins():
            print("Please insert coins")
            quarter = float(input("How many quarters?: "))
            dime = float(input("How many dime?: "))
            nickel = float(input("How many nickel?: "))
            penny = float(input("How many penny?: "))
            quarter *= 0.25
            dime *= 0.1
            nickel *= 0.05
            penny *= 0.01
            total_value = quarter + dime + nickel + penny
            total_value = round(total_value, 2)

            # TODO: 5. Check if transaction successful
            global cost_per_drink, resources

            if total_value < cost_per_drink:
                print("Sorry that's not enough money. Money refunded.")
            elif total_value >= cost_per_drink:
                balance = round(total_value - cost_per_drink, 2)
                if total_value > cost_per_drink:
                    print(f"Here is {balance} dollars in change")
                resources["money"] += cost_per_drink
                make_coffee()


        # TODO: 3. Check resources are sufficient
        if water_required < resources["water"]:
            if milk_required < resources["milk"]:
                if coffee_required < resources["coffee"]:
                    process_coins()
                    # calling the function here
                else:
                    print("sorry there is not enough milk")
            else:
                print("sorry there is not enough milk")
        else:
            print("sorry there is not enough water")

    else:
        print("watch for the typo !")