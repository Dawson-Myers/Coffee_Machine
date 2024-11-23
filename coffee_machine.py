from menu import MENU
from resources import resources


def format_menu(menu_item):
    item_espresso = MENU["espresso"]
    item_latte = MENU["latte"]
    item_cappuccino = MENU["cappuccino"]
    if menu_item == 'espresso':
        return item_espresso
    elif menu_item == 'latte':
        return item_latte
    elif menu_item == 'cappuccino':
        return item_cappuccino
    else:
        print("invalid selection")

# Variables for format_menu()
espresso = format_menu("espresso")
latte = format_menu("latte")
cappuccino = format_menu("cappuccino")


def menu_ingredients(menu_item):
    ingredients = menu_item["ingredients"]
    return ingredients

# Variable for menu_ingredients()
espresso_ingredients = menu_ingredients(espresso)
latte_ingredients = menu_ingredients(latte)
cappuccino_ingredients = menu_ingredients(cappuccino)


def menu_cost(menu_item):
    cost = menu_item["cost"]
    return cost

# Variables for menu_cost()
espresso_cost = menu_cost(espresso)
latte_cost = menu_cost(latte)
cappuccino_cost = menu_cost(cappuccino)



def format_resources(item):
    water_resource = resources["water"]
    milk_resource = resources["milk"]
    coffee_resource = resources["coffee"]
    if item == "water":
        return water_resource
    elif item == "milk":
        return milk_resource
    elif item == "coffee":
        return coffee_resource
    else:
        print("invalid inventory item")

# Variables for format_resources()
water = format_resources("water")
milk = format_resources("milk")
coffee = format_resources("coffee")


def coffee_machine():
    cust_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if cust_order == "off":
        return make_coffee == False
    elif cust_order == "espresso":
        return espresso
    elif cust_order == "latte":
        return latte
    elif cust_order == "cappuccino":
        return cappuccino
    elif cust_order == "report":
        report()
    else:
        print("invalid selection")


def report():   
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g')    


def check_resources():
    no_water = "Sorry not enough water."
    no_coffee = "Sorry not enough coffee."
    no_milk = "Sorry not enough milk."
    for ingredients in espresso_ingredients:
        if water >= espresso_ingredients["water"]:
            if coffee >= espresso_ingredients["coffee"]:
                return espresso_ingredients
            else:
                return no_coffee
        else:
            return no_water
    for ingredients in latte_ingredients:
        if water >= latte_ingredients["water"]:
            if coffee >= latte_ingredients["coffee"]:
                if milk >= latte_ingredients["milk"]:
                    return latte_ingredients
                else:
                    return no_milk
            else:
                return no_coffee
        else:
            return no_water
        
    for ingredients in cappuccino_ingredients:
        if water >= cappuccino_ingredients["water"]:
            if coffee >= cappuccino_ingredients["coffee"]:
                if milk >= cappuccino_ingredients["milk"]:
                    return cappuccino_ingredients
                else:
                    return no_milk
            else:
                return no_coffee
        else:
            return no_water

# FIXME: Needs to update inventory items 
def update_resource(water, coffee, milk):
    ingredients = water, coffee, milk         
    for ingredients in espresso_ingredients:
        water -= espresso_ingredients["water"]
        coffee -= espresso_ingredients["coffee"]
    for ingredients in latte_ingredients:
        water -= latte_ingredients["water"]
        coffee -= latte_ingredients["coffee"]
        milk -= latte_ingredients["milk"]
    for ingredients in cappuccino_ingredients:
        water -= cappuccino_ingredients["water"]
        coffee -= cappuccino_ingredients["coffee"]
        milk -= cappuccino_ingredients["milk"]
    return ingredients

        

make_coffee = True
while make_coffee:
    make_drink = coffee_machine()

    if make_drink == espresso:
        check_resources()
        update_resource(water, coffee, milk)
        print("you chose espresso")
        print(f"Cost: ${espresso_cost:.2f}")
        report()
    if make_drink == latte:
        check_resources()
        update_resource(water, coffee, milk)
        print("you chose latte")
        print(f"Cost: ${latte_cost:.2f}")
        report()
    if make_drink == cappuccino:
        check_resources()
        update_resource(water, coffee, milk)
        print("you chose cappuccino")
        print(f"Cost: ${cappuccino_cost:.2f}")
        report()





'''
TODO: 
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    a. Check the user’s input to decide what to do next.
    b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.


TODO:
2. Turn off the Coffee Machine by entering “off” to the prompt.
    a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        the machine. Your code should end execution when this happens.

TODO: 
3. Print report.
    a. When the user enters “report” to the prompt, a report should be generated that shows
        the current resource values. e.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5

TODO:
4. Check resources sufficient?
    a. When the user chooses a drink, the program should check if there are enough
        resources to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
        not continue to make the drink but print: “Sorry there is not enough water.”
    c. The same should happen if another resource is depleted, e.g. milk or coffee.

TODO: 
5. Process coins.
    a. If there are sufficient resources to make the drink selected, then the program should
        prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
        pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

TODO:
6. Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected.
        E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        program should say “Sorry that's not enough money. Money refunded.”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
        machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
    c. If the user has inserted too much money, the machine should offer change.
        E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
        places.

TODO:
7. Make Coffee.
    a. If the transaction is successful and there are enough resources to make the drink the
        user selected, then the ingredients to make the drink should be deducted from the
        coffee machine resources.

        E.g. report before purchasing latte:
        Water: 300ml
        Milk: 200ml
        Coffee: 100g
        Money: $0

        Report after purchasing latte:
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5

    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
        latte was their choice of drink.
'''




# print(espresso)
# print(latte)
# print(cappuccino)
# print()
# print(espresso_ingredients)
# print(latte_ingredients)
# print(cappuccino_ingredients)
# print()
# print(espresso_cost)
# print(latte_cost)
# print(cappuccino_cost)
# print()
# print(water)
# print(milk)
# print(coffee)




"""
~~ Formats Menu into passable variables ~~
    Variables Belows:
     - espresso
     - latte
     - cappuccino
"""
""" 
~~ Formats Menu Ingredients into passable variables ~~
    Variables Below: 
     - espresso_ingredients
     - latte_ingredients
     - cappuccino_ingredients
"""
"""
~~ Formats Menu Item Cost into passable variables ~~
    Variables Below:
     - espresso_cost
     - latte_cost
     - cappuccino_cost
"""
"""
~~ Formats Resource Data into passable variables ~~
    Variables Below:
     - water
     - milk
     - coffee
"""