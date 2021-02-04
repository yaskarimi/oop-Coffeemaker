from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
process = CoffeeMaker()
purchase = MoneyMachine()
is_on = True


while is_on:
 answer = input("What would you like? " + items.get_items())
 if answer == "report":
    process.report()
    purchase.report()
 elif answer == "off":
     is_on = False
 else:
  drink = items.find_drink(answer)
  item = MenuItem(drink.name , drink.ingredients["water"],
                  drink.ingredients["milk"],drink.ingredients["coffee"],
                  drink.cost)
  if process.is_resource_sufficient(drink):
    if purchase.make_payment(drink.cost):
     process.make_coffee(drink)


