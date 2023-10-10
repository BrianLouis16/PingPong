from helloword import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def quarters():
    amount = int(input("How many quarters do you have?: ")) * 0.25
    return amount


def dimes():
    amount = int(input("How many dimes do you have?: ")) * 0.10
    return amount


def nickel():
    amount = int(input("How many nickel do you have?: ")) * 0.05
    return amount


def pennies():
    amount = int(input("How many pennies do you have?: ")) * 0.01
    return amount


def get_coffee():
    user = input("Which coffee would you like (espresso/latte/cappuccino)?: ")
    if user in MENU:
        coffee_info = MENU[user]
        return coffee_info
    else:
        return None



while True:
    coffee_info = get_coffee()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if coffee_info is not None:
        cost = coffee_info["cost"]

        water_cost = coffee_info["ingredients"]["water"]

        coffee_cost = coffee_info["ingredients"]["coffee"]

        if "milk" in coffee_info["ingredients"]:
            milk_cost = coffee_info["ingredients"]["milk"]
        else:
            milk_cost = 0

        change = round(quarters() + dimes() + nickel() + pennies(), 2)

        if change >= cost:
            change = change - cost

            print(f"You have enough. Your change is {change}")
            # Deduct resources

            water -= water_cost
            milk -= milk_cost
            coffee -= coffee_cost
            if water <= 0:
                print("You do not have enough water. ")
                user = input("Would you like to add some water y/n .: ").lower()
                if user == "yes":
                    water += 450
            elif milk <= 0:
                print("You do not have enough coffee.")
                user = input("Would you like to add some water y/n .: ").lower()
                if user == "yes":
                    milk += 450
            elif coffee <= 0:
                print("You do not have enough coffee")
                user = input("Would you like to add some coffee? y/n .: ").lower()
                if user == "yes":
                    water += 450
        else:
            print("Not enough, you have been refunded")
    else:
        print("Invalid coffee choice")
        get_coffee()
    print("Thank you for buying from the vending machine!")
    again = input("Would you like to buy another coffee? (yes/no) : ").lower()
    if again != "yes":
        break
