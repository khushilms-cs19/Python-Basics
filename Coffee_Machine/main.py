import art
import beverage_data
import os

print_coffee_given={
    "latte": art.latte_ready,
    "espresso":art.espresson_ready,
    "cappuccino":art.cappuccino_ready,
}


def clear_screen():
    if os.name=="nt":
        _=os.system("cls")
    else:
        _=os.system("clear")


def ask_for_coffee():
    print("Which type of coffee would you like to have?")
    print("A: Espresso\nB: Latte\nC: Cappuccino\nD: Exit\nE: Report")
    coffee_choice=input("Enter your choice:").upper()
    if coffee_choice=="A":
        return "espresso"
    elif coffee_choice=="B":
        return "latte"
    elif coffee_choice=="C":
        return "cappuccino"
    elif coffee_choice=="D":
        exit(0)
    elif coffee_choice=="E":
        return "report"
    else:
        print("Enter a valid option")  
        return "invalid"  


def check_for_resources(coffee):
    reso=beverage_data.MENU[coffee]["ingredients"]
    for key in reso:
        if resources[key]<reso[key]:
            print("There is no enough {} for {}, Please come again after some time".format(key,coffee))
            return False
    return True        




def show_report():
    print("{}: {}ml".format("Milk",resources["milk"]))
    print("{}: {}ml".format("Water",resources["water"]))
    print("{}: {}g".format("Coffee",resources["coffee"]))
    print("{}: ${}".format("Money",resources["money"]))


def ask_for_money(coffee):
    print("Insert the coins:")
    quats=int(input("The number of Quaters:"))
    dimes=int(input("The number of Dimes:"))
    nicks=int(input("The number of Nickels:"))
    pennies=int(input("The number of Pennies:"))
    total_money_inserted=(0.25*quats)+(dimes*0.1)+(nicks*0.05)+(pennies*0.01)
    if total_money_inserted>=beverage_data.MENU[coffee]["cost"]:
        print_coffee_given[coffee]
        change_remaining=total_money_inserted-beverage_data.MENU[coffee]["cost"]
        resources_present=check_for_resources(coffee)
        if resources_present:
            for key in beverage_data.MENU[coffee]["ingredients"]:
                resources[key]-=beverage_data.MENU[coffee]["ingredients"][key]
        else:
            print("The money inserted ${}, is refunded.".format(total_money_inserted))
            return
        clear_screen()
        print(print_coffee_given[coffee])
        resources["money"]+=beverage_data.MENU[coffee]["cost"]   
        print("The {} you ordered is ready. Enjoy your day!!.\nThe change is: ${:.2f}".format(coffee,change_remaining))
    else:
        print("Sorry, the money inserted is not enough for the beverage you ordered.") 
        print("The money inserted ${} , is refunded.".format(total_money_inserted))
    return   

        



resources={
    "milk": 200,
    "water": 100,
    "coffee": 100,
    "money":0
}

continueToMake=True
while continueToMake:
    clear_screen()
    print(art.coffee_machine)
    coffee=ask_for_coffee()
    if coffee=="report":
        clear_screen()
        print(art.coffee_machine)
        show_report()
        input("Press Enter to continue")
        continue
    elif coffee=="invalid":
        continue
    clear_screen()
    print(art.coffee_machine)
    print(coffee)
    ask_for_money(coffee)
    input("Press Enter to continue")
    