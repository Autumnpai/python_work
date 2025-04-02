while True:
    num1 = input('Please input a number: ')
    try:
        num1 = int(num1)
    except ValueError:
        print('Sorry, please input numbers only! Thanks!')
    else:
        break

while True:
    num2 = input('Please input another number: ')
    try:
        num2 = int(num2)
    except ValueError:
        print('Sorry, please input numbers only! Thanks!')
    else:
        break


print(f'{num1} + {num2} = {num1 + num2}')