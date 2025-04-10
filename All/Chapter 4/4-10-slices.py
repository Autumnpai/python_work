cube_num = []
for num in range(1, 11):
    cube_num.append(num**3)

print(cube_num)

print('\nThe first three items in the list are:')
print(cube_num[:3], '\n')

print('Three items from the middle of the list are:')
print(cube_num[4:7], '\n')

print('The last three items in the list are:')
print(cube_num[-3:])