MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 30,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 35,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order):
    for i in order:
        if order[i]>=resources[i]:
            print(f"sorry not enough {i}")
            return False
    return True

def process_coins():
    total=int(input("Plz pay money"))
    return total

def is_trans(cost_rec,drink_cost):
 if cost_rec>=drink_cost:
        change=round(cost_rec-drink_cost)
        print(f"Here is {change} in change")
        global profit
        profit+=drink_cost
        return  True
 else:
        print("Insufficient balance")


def make_cof(drink_name,order_ing):
   for i in order_ing:
       resources[i]-=order_ing[i]
   print(f"Here is ur {drink_name}")


is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice== "off":
      is_on= False
    elif choice=="report":
        print(f"Water: {resources['water'] }ml")
        print(f"Milk: {resources['milk'] }ml")
        print(f"Coffee: {resources['coffee'] }g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment=process_coins()
           if is_trans(payment,drink["cost"]):
               make_cof(choice,drink['ingredients'])
