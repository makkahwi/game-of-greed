import random
from collections import Counter

class GameLogic:

  @staticmethod
  def get_scorers(tuple_int):
    """
    A method that returns the roll's score based on the rules of the game.
    INPUT: Tuple of integers that represent a dice roll
    OUTPUT: Integer representing the roll's score
    """
    ctr = Counter(tuple_int)
    score = 0
    count = 0
    for dices, rep in ctr.items():
      # Straight one, two, three, four, five, six
      if ctr.most_common()[0][1] == 1 and len(ctr.items()) == 6:
        score = 1500
      # Six Ones
      if dices == 1 and rep == 6:
        score += 4000
      # Five Ones
      if dices == 1 and rep == 5:
        score += 3000
      # Four Ones
      if dices == 1 and rep == 4:
        score += 2000
      # Three Ones
      if dices == 1 and rep == 3:
        score += 1000
      # Six of a kind
      if rep == 6 and dices != 1:
        score += 400*dices
      # Five of a kind
      if rep == 5 and dices != 1:
        score += 300*dices
      # Four of a kind
      if rep == 4 and dices != 1:
        score += 200*dices
      # Three of a kind
      if rep == 3 and dices != 1:
        score += 100*dices
      # Single Five
      if dices == 5 and rep !=3 and rep != 4 and rep != 5 and rep != 6:
        score += (50*rep)
      # Single One
      if dices == 1 and rep != 3 and rep != 4 and rep != 5 and rep != 6:
        score += (100*rep)
      # Three pairs of a kind
      if rep == 2:
          count += 1
      if count == 3:
        score = 1500
    return score

  @staticmethod
  def roll_dice(dices):
    """
    A method that returns a tuple of integers representing the dice roll
    INPUT: Integer between 1 and 6
    OUTPUT: Tuple of random values between 1 and 6
    """
    random_list_values = [random.randint(1,6) for _ in range(dices)]
    return tuple(random_list_values)
    # random_list_values = []
    # for _ in range(1,dices+1):
    #   random_int = random.randint(1,dices)
    #   random_list_values.append(random_int)
    # random_values = tuple(random_list_values)
    # return random_values


if __name__ == '__main__':
  # print("dices:",dices)
  # print("rep:",rep)
  # print(ctr)
  # Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
  # [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]
  tuple_int = GameLogic.roll_dice(4)
  print (tuple_int)
  print(GameLogic.get_scorers(tuple_int))