from random import choice

num_letter = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E')

result = []
for each in range(4):
    result.append(choice(num_letter))

print(f'{result[0]}{result[1]}{result[2]}{result[3]} won the prize!')

