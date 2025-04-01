while True:
    num1 = input('Please input a number (q for quit): ')
    if num1 == 'q':
        break
    try:
        num1 = int(num1)
    except ValueError:
        print('Sorry, please input numbers only! Thanks!')
    else:
        while True:
            num2 = input('Please input another number (q for quit): ')
            if num2 == 'q':
                break
            try:
                num2 = int(num2)
            except ValueError:
                print('Sorry, please input numbers only! Thanks!')
            else:
                print(f'{num1} + {num2} = {num1 + num2}')
                break