

from game_of_greed.game_logic import GameLogic
from game_of_greed.game_logic import Banker


class Game:

    def __init__(self, roller = None):
        self.roller = roller

    def play(self):
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            round = 1
            newBank = Banker()
            while (round <= 6):
                print(f'Starting round {round}')
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))
                # print(*rolled_dice, sep=',')
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if (decision == "q"):
                    if (round > 1):
                        print(f'Total score is {newBank.balance} points')
                    print(f'Thanks for playing. You earned {newBank.balance} points')
                    break
                else: 
                    decisionList = list(map(int, str(decision)))
                    unpacked = GameLogic.calculate_score(decisionList)
                    newBank.shelf(unpacked)
                    print(f'You have {unpacked} unbanked points and {6-len(decisionList)} dice remaining')
                    decisionBankedPoint = input("(r)oll again, (b)ank your points or (q)uit ")
                    BankedPoint = newBank.bank()
                    print(f'You banked {unpacked} points in round 1')
                    print(f'Total score is {newBank.balance} points')
                round +=1

                
                 


if __name__ == "__main__":
    
    game = Game(GameLogic.roll_dice)
    game.play()