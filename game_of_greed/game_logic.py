
class GameLogic:
  def __init__(self):
    pass

  def calculate_score(roll):
    pass

  def roll_dice(dices):
    pass

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


    