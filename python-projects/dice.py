import random

def roll_dice():
    
    dice_drawing = {
        1: (
            " _______",
            "|   1   |",
            "|   @   |",
            "|       |",
            "|_______|",
        ),
        2: (
            " _______",
            "| @     |",
            "|   2   |",
            "|     @ |",
            "|_______|",
        ),
        3: (
            " _______",
            "| @ 3   |",
            "|   @   |",
            "|      @|",
            "|_______|",
        ),
        4: (
            " _______",
            "| @   @ |",
            "|   4   |",
            "| @   @ |",
            "|_______|",
        ),
        5: (
            " _______",
            "| @ 5 @ |",
            "|   @   |",
            "| @   @ |",
            "|_______|",
        ),
        6: (
            " _______",
            "| @   @ |",
            "| @ 6 @ |",
            "| @   @ |",
            "|_______|",
        ),
    }
    
    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes/No): ")
roll_dice()