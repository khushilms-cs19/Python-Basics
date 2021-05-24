from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte=MenuItem("latte",200,150,24,2.5)

espresso=MenuItem("espresso",50,0,18,1.5)

cappuccino=MenuItem("cappuccino",250,100,24,3.0)
coffee_maker_machine=CoffeeMaker()
money_reserve=MoneyMachine()

menu=Menu()
machine_working=True
while machine_working:
    print("The items available are : ")
    print(menu.get_items())
    coffee_ordered=input("Enter the coffee you want:").lower()
    
    if coffee_ordered=="report":
        print("The contents of the coffee machine is:")
        coffee_maker_machine.report()
        money_reserve.report()
        continue
    elif coffee_ordered=="off":
        exit()

    drink_ordered=menu.find_drink(coffee_ordered)
    if coffee_maker_machine.is_resource_sufficient(drink_ordered):
        if money_reserve.make_payment(drink_ordered.cost):
            coffee_maker_machine.make_coffee(drink_ordered)
        else:
            continue
    else:
        continue      




