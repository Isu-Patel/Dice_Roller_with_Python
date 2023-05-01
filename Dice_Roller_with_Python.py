import random

# Define a function to roll the dice
def roll_dice():
    # Generate a random number between 1 and 6
    roll = random.randint(1, 6)
    return roll

# Prompt the user to roll the dice
input("Press Enter to roll the dice...")

# Roll the dice and display the result to the user
result = roll_dice()
print(f"You rolled a {result}!")
