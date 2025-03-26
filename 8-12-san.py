def san(*toppings):
    """making sandwiches with toppings"""
    for topping in toppings:
        print(f'A {topping} sandwich is ordered.')
    print()

san("sausage")
san('pepperroni', 'veg', 'pineapple', 'ham')
san('ham', 'cheese')