from random import randint

class Die:
    """a dice class"""

    def __init__(self, sides=6):
        """initialize"""
        self.sides = sides

    def roll_die(self):
        """roll the dice"""
        print(randint(1, self.sides))


six_dice = Die()
ten_dice = Die(10)
twenty_dice = Die(20)


print(f"Roll the six-sides dice 10 times: ")
for each in range(10):
    six_dice.roll_die()

print(f'Roll the ten-sides dice 10 times: ')
for each in range(10):
    ten_dice.roll_die()

print(f'Roll the twenty-sides dice 10 times: ')
for each in range(10):
    twenty_dice.roll_die()