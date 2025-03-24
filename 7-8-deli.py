san_ords = ['chicken', 'beef', 'pork', 'fish', 'veggie', 'tuna']
finished_sandwiches = []
while san_ords:
    current_sandwich = san_ords.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"    {sandwich} sandwich")