fav_piz = ['pepperoni', 'veg', 'pineapple', 'cheese']
# for piz in fav_piz:
#     print(f'I like {piz} pizza!')

# print('I really love pizza!')

friend_pizza = fav_piz[:]

fav_piz.append('sausage')
friend_pizza.append('spinich')

print(f'My favorite pizzas are:')
for piz in fav_piz:
    print(piz)

print(f"\nMy friend's favorite pizzas are:")
for fpiz in friend_pizza:
    print(fpiz)

