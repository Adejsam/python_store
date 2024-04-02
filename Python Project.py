
#   SIMULATING AN ONLINE STORE
price_of_goods = {'bottle water':200,'soda':150,'soaps':200,'detergents':250,'insecticides':1200,
                  'cereals':900,'body spray':900,'toothpaste':350,'polish':500,'body cream':300,'shampoo':600,
                  'flour':20000,'rice':35000,'bread':400,'chips':1500,'jelly':700,'napkins':400,'tissues':300,
                  'Garri':30000,'beans':28000,'sachet milk':50,'tomato sauce':800,'hot dogs':700,'soy sauce':1000,
                  'canned milk':400,'chocolate syrup':2000,'mustard':70,'butter':500,'cheese':400,'yogurt':200,
                  'honey':600,'peanut butter':400,'sardines':350,'ketchup':1700,'mayonnaise':1200,'sour cream':800,
                  'spaghetti':250}
stock_of_goods = {'bottle water': 70000,'soda': 100000,'soaps':500,'detergents':2500,'insecticides':900,
                  'cereals':9000,'body spray':7000,'toothpaste':3500,'polish':2000,'body cream':3000,'shampoo':3000,
                  'flour':2000,'rice':3500,'bread':4000,'chips':15000,'jelly':7000,'napkins':4000,'tissues':10000,
                  'Garri':3000,'beans':2800,'sachet milk':50000,'tomato sauce':8000,'hot dogs':7000,'soy sauce':9000,
                  'canned milk':4000,'chocolate syrup':20000,'mustard':700,'butter':5000,'cheese':4000,'yogurt':2000,
                  'honey':600,'peanut butter':4000,'sardines':3500,'ketchup':1000,'mayonnaise':1000,'sour cream':8000,
                  'spaghetti':2500}
stock_cart = {}
cart = {}
remaining_stock = []
my_cart = []
price_cart = []
quantity_cart = []
cost_per_good = []
total_cost = []
while True:
    print('_________________________________________________________________________________________')
    print('WELCOME TO MELISSA ONLINE STORE.')
    instruction = ('''
Dear customers note that melissa stores is currently running a promo
Buy goods worth 5000 NGN and above and get 15% discount 
Buy goods worth 3500 NGN and get 10% discount
Buy goods worth between 2000 and 3500 NGN and get 5% discount
_____________________________________________________________________________________________
_____________________________________________________________________________________________
ENTER:
1. View items available
2. Place an order
3. Exit Store
______________________________________________________________________________________________
______________________________________________________________________________________________
''')
    print(instruction)
    choice =input('Enter a number of your choice between 1,2 and 3: ')
    if choice == '1':
        print('{:>10}{:>13}'.format('GOODS', ' PRICE'))
        for goods, price in price_of_goods.items():
            print('{:>10} {:>10}'.format(goods, price))
        continue
    if choice == '3':
        print('Thanks for patronizing melissa stores')
        quit()
    elif choice == '2':
        while True:
            goods = input('Enter what you want to purchase: ')
            goods.lower()
            my_cart.append(goods)
            while goods not in price_of_goods:
                print('Product not available')
                goods = input('Enter what you want to purchase: ')
            if goods in price_of_goods:
                print('The price of',goods,'is',price_of_goods[goods])
                price_cart.append(price_of_goods[goods])
            quantity = eval(input('How many do you want to purchase: '))
            quantity_cart.append(quantity)
            cart[goods]= quantity
            stock_cart[goods]= stock_of_goods[goods]
            cost = price_of_goods[goods] * quantity
            cost_per_good.append(cost)
            if quantity > stock_of_goods[goods]:
                print("quantity requested is more than stock available")
            option = input("Do you want to purchase more, yes or no: ")
            option.lower()
            print()
            if option == 'yes':
                continue
            if option == 'no':
                confirm = input('Are you sure you want confirm this shopping list,yes or no: ')
                confirm.lower()
                if  confirm == 'no':
                    continue
                if confirm == 'yes':
                    for i in cart:
                        cart[i]= stock_cart[i] - cart[i]
                        remaining_stock.append(cart[i])
            break
    break
total = sum(cost_per_good)
print('___________________________________________________________________________________')
print(' '*25 + 'MY CART')
print('____________________________________________________________________________________')

import pandas as pd
customers_data = pd.DataFrame({
        'GOODS': my_cart,
        'PRICE': price_cart,
        'QUANTITY': quantity_cart,
        'COST': cost_per_good,
})
print(customers_data)
print('____________________________________________________________________________________________')
print("TOTAL COST = ", total, 'NGN')
print('_____________________________________________________________________________________________')
if total >= 5000:
    discount = total - (total * 12)/100
    print('You have been rewarded with a 12% discount.')
    print('Amount to be payed =', discount, 'NGN')
if total == 3500:
    discount = total - (total * 10)/100
    print('You have been rewarded with a 10% discount.')
    print('Amount to be payed =', discount, 'NGN')

elif total <= 3500 and total >= 2000:
    discount = total - (total * 5)/100
    print('You have been rewarded with a 5% discount.')
    print('Amount to be payed', discount, 'NGN')
print('Thanks for shopping at melissa store. Your goods should be delivered in two days')
print()
customers_data.to_csv('goods price quantity cost.xlsx')