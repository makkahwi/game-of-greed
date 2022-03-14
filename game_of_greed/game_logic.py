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
        
        occurance = []
        threes = []

        # This is to identify how many occurrences there are of each of the numbers
        for no in roll:
            occurance.append(0)

        for no in roll:
            occurance[no - 1] = int(occurance[no - 1]) + 1

        # This is to identify how many numbers did occur three times or more
        for no in occurance:
            if no >= 3:
                threes.append(no)
            else:
                threes.append(0)

        # Check if the roll is a sequence of 1 to 6
        if set(roll) == set([1, 2, 3, 4, 5, 6]):
            return 1000

        # Check if the roll has pairs
        elif len(roll) == 6 and len(set(roll)) == 3 and set(occurance) == set([0, 2]):
            return 1000

        # Check if the roll has six ones
        elif roll == [1, 1, 1, 1, 1, 1]:
            return 1000000

        # Check if the roll has occurrences of three or more
        elif len(list(filter(lambda no: no > 0, threes))) > 0:
            total = 0
            i = 1

            for no in threes:
                if i == 1 and no >= 3:
                    total = total + 1000
                elif no > 0:
                    total = total + (i * 100)

                i = i + 1

            return total

        # Check if the roll has any fives or ones
        elif 1 in roll or 5 in roll:
            total = 0
            total = total + (len(list(filter(lambda no: no == 1, roll))) * 100)
            total = total + (len(list(filter(lambda no: no == 5, roll))) * 50)
            return total

        # Return 0 points for not meeting any of the rules above
        else:
            return 0

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
  '''
  Class Banker with initial values of 0 for both Balance and shelved 
  three methods shelf , bank , clear_shelf
  '''
  def __init__(self,balance = 0 , shelved = 0):
      self.balance = 0
      self.shelved = 0

  def shelf(self,temPoint):
    '''
    shelf method 
    Input : the amount of points (integer) to add to shelf.
    shelf temporarily store unbanked points
    '''
    self.shelved += temPoint
  

  def bank(self):
    '''
    bank method 
    its  add any points on the shelf to total and reset shelf to 0.
    bank output should be the amount of points added to total from shelf.
    '''
    self.balance += self.shelved
    self.clear_shelf()
    return self.balance
    
 
  def clear_shelf(self):
    '''
    clear_shelf method remove all unbanked points.
    '''
    self.shelved = 0