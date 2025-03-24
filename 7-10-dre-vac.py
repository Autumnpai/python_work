vacs = {}
while True:
    user = input("What's your name? ")
    vacation = input("Where do you want to go? ")
    vacs[user] = vacation
    repeat = input("Do you want to invite anther person to the poll? (yes/no) ")
    while repeat != 'no' and repeat != 'yes':
        print("Invalid input. Please enter 'yes' or 'no'.")
        repeat = input("Do you want to invite anther person to the poll? (yes/no) ")

    if repeat == 'no':
        break


print("\n--- Poll Results ---")
for user, vacation in vacs.items():
    print(f"{user.title()} wants to go to {vacation.title()}.")