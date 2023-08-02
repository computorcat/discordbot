import random

class Dnd:
    def __init__(self):
        pass
    
    def diceRoll(self, dice):
        # this will usually be in the format of 1d20
        # 1 = the number of dice, d20 = the number of sides
        dice = dice.split('d')
        num = int(dice[0])
        sides = int(dice[1])
        rolls = []
        for i in range(num):
            roll = random.randint(1, sides)
            rolls.append(roll)
        # return the rolls as a \n seperated string
        rolls = '\n'.join(str(roll) for roll in rolls)
        # add the total to the end when the number of dice is greater than 1 
        return rolls
    

if __name__ == "__main__":
    dice = Dnd.diceRoll('5d20')