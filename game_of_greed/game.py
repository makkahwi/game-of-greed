from collections import Counter

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self, roller=None):
        self.roller = roller


    def play(self):
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            Dices = 6
            round = 1
            rollagain = 0
            newBank = Banker()
            while (True):
                if (rollagain == 0):
                    print(f'Starting round {round}')
                    Dices = 6
                print(f'Rolling {Dices} dice...')
                # to print the Rolling dice
                rolled_dice = self.roller(Dices)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))

                # check for the Zilch Case 
                if (GameLogic.calculate_score(rolled_dice) == 0):
                    print("Zilch!!! Round over")
                    break
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if decision != "q": 
                    decisionList = list(map(int, str(decision)))

                    # check for the cheater or typo 
                    ctr = Counter(rolled_dice)
                    ctr2 = Counter(decisionList)
                    for i in ctr2.keys():
                        if (i not in ctr.keys()) or (ctr2[i] > ctr[i]) :
                            print("Cheater!!! Or possibly made a typo...")
                            print(",".join(nums))
                            first_decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                            decisionList = tuple(map(int, str(first_decision)))
                    unpacked = GameLogic.calculate_score(decisionList)
                    newBank.shelf(unpacked)
                    Dices = Dices - len(decisionList)
                    print(f'You have {newBank.shelved} unbanked points and {Dices} dice remaining')
                    decision = input("(r)oll again, (b)ank your points or (q)uit ")
                    

                    # check for the bank decision 
                    if decision == "b":
                        print(f'You banked {newBank.shelved} points in round {round}')
                        newBank.bank() 
                        print(f'Total score is {newBank.balance} points')
                        rollagain = 0
                    elif (decision =="r"):
                        rollagain = 1
                        if (Dices == 0):
                            Dices = 6
                        continue

                # check forf the quitter decision 
                if (decision  == "q"):
                    if (round > 1 or newBank.shelved !=0 ) :
                        print(f'Total score is {newBank.balance} points')
                    print(f'Thanks for playing. You earned {newBank.balance} points')
                    break
                round +=1

                
                 


if __name__ == "__main__":
    
    game = Game(GameLogic.roll_dice)
    game.play()