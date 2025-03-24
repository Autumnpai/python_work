san_ords = ['chicken', 'pastrami', 'beef', 'pork', 'pastrami', 'pastrami', 'fish', 'veggie', 'tuna']
print("Sorry, we are out of pastrami.")
while 'pastrami' in san_ords:
    san_ords.remove('pastrami')

finished_sandwiches = []
while san_ords:
    current_sandwich = san_ords.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"    {sandwich} sandwich")