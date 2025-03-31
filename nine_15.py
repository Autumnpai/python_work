from random import choice

num_letter = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E')

result = []
# pull the result without repetition. 
while len(result) < 4:
    ran_item = choice(num_letter)
    if ran_item not in result:
        result.append(ran_item)

print(f'{result[0]}{result[1]}{result[2]}{result[3]} won the prize!')

# pull the same result with same numbers/letters, no need same order.
new_result = []
times = 0
while set(new_result) != set(result):
    new_result = []
    while len(new_result) < 4:
        ran_item = choice(num_letter)
        if ran_item not in new_result:
            new_result.append(ran_item)
    times += 1
print(f"The {new_result[0]}{new_result[1]}{new_result[2]}{new_result[3]} is gotten!")

print(f"{times} times was run to give you the winning ticket.")
