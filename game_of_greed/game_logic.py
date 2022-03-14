import random

class GameLogic:
  def __init__(self):
    pass

  def calculate_score(roll):
    """
    A method that returns the roll's score based on the rules of the game.
    INPUT: Tuple of integers that represent a dice roll
    OUTPUT: Integer representing the roll's score
    """
    pass

  @staticmethod
  def roll_dice(dices):
    """
    A method that returns a tuple of integers representing the dice roll
    INPUT: Integer between 1 and 6
    OUTPUT: Tuple of random values between 1 and 6
    """
    random_list_values = []
    for _ in range(1,dices+1):
      random_int = random.randint(1,dices)
      random_list_values.append(random_int)
    random_values = tuple(random_list_values)

    return random_values

class Banker:
  total = 0

  def __init__(self):
    pass

  def shelf(temPoint):
    """
    A method used to store the points in each roll
    INPUT: Integer that represents the points to be added to the shelf
    OUTPUT: Temporary store unbanked points
    """
    pass

  def bank(unbanked):
    """
    A method that is used to add the points gained in the roll to the total, and reset the shelf to zero
    INPUT: Nothing
    OUTPUT: Amount of points added to total from shelf
    """
    pass

  def clear_shelf():
    """
    A method used to clear all unbanked points
    INPUT: Nothing
    OUTPUT: 
    """
    pass


if __name__ == '__main__':
  roll1 = GameLogic.roll_dice(1)
  print(roll1)
