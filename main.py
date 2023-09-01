from menu import MENU, resources

# Money value
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

# Price
espresso = MENU['espresso']['cost']
cappuccino = MENU['cappuccino']['cost']
latte = MENU['latte']['cost']

check = True

def coffe_machine():
    case = 0
    while True:
        ask = input("What would you like? (espresso/latte/cappuccino): ")
        if ask == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${case}")
            continue
        elif ask == 'espresso':
            if resources['water'] >= 50 and resources['coffee'] >= 18:
                coff = ask
                ask = espresso
                case += espresso
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            else:
                print("Sorry there is not enough water.")
                continue
        elif ask == 'cappuccino':
            if resources['water'] >= 250 and resources['milk'] >= 100 and resources['coffee'] >= 24:
                coff = ask
                ask = cappuccino
                case += cappuccino
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            else:
                print("Sorry there is not enough water.")
                continue
        elif ask == 'latte':
            if resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
                coff = ask
                ask = latte
                case += latte
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            else:
                print("Sorry there is not enough water.")
                continue
        elif ask == 'q':
            break
        else:
            print("Please enter the correct words.")
            continue

        print("Please insert coins.")
        quar = int(input("How many quarters?: "))
        dim = int(input("How many dimes?: "))
        nick = int(input("How many nickles?: "))
        pen = int(input("How many pennies?: "))

        price = (quar * 0.25) + (dim * 0.10) + (nick * 0.05) + (pen * 0.01)

        cash_back = round((price - ask),2)

        print(f"Here is ${cash_back} in change.")
        print(f"Here is your {coff}🥤. Enjoy!")
coffe_machine()





# TODO: 1. Print report of all coffee machine resources
# TODO: 2. Check resources sıfficient to make drink order.