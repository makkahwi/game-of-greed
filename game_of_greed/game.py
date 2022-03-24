from collections import Counter

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self, roller = None):
        self.roller = roller or GameLogic.roll_dice
        self.banker = Banker()
        self.game_logic = GameLogic()
        self.round = 0
        self.total_score = 0

    def play(self):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")

        wanna_play = input()
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            Dices = 6
            self.round = 1
            rollagain = 0
            while True:
                # if self.round > 20:
                #     return "q"
                if self.total_score > 1000:
                    return "q"

                if rollagain == 0:
                    print(f"Starting round {self.round}")
                    Dices = 6
                print(f"Rolling {Dices} dice...")
                # to print the Rolling dice
                rolled_dice = self.roller(Dices)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))

                print("*** " + ",".join(nums))

                # check for the Zilch Case
                if GameLogic.get_scorers(rolled_dice) == 0:
                    print("Zilch!!! Round over")
                    break
                print("Enter dice to keep, or (q)uit:")
                decision = input()
                if decision != "q":
                    decisionList = list(map(int, str(decision)))

                    # check for the cheater or typo
                    ctr = Counter(rolled_dice)
                    ctr2 = Counter(decisionList)
                    for i in ctr2.keys():
                        if (i not in ctr.keys()) or (ctr2[i] > ctr[i]):
                            # print("Cheater!!! Or possibly made a typo...")
                            print("*** " + ",".join(nums))
                            print("Enter dice to keep, or (q)uit:")
                            first_decision = input()
                            decisionList = tuple(map(int, str(first_decision)))
                    unpacked = str(GameLogic.get_scorers(decisionList))
                    self.banker.shelf(unpacked)
                    Dices = Dices - len(decisionList)
                    print(f"You have {self.banker.shelved} unbanked points and {Dices} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    decision = input()

                    # check for the bank decision
                    if decision == "b":
                        print(f"You banked {self.banker.shelved} points in round {self.round}")
                        self.banker.bank()
                        self.total_score += int(self.banker.balance)
                        print(f"Thanks for playing. You earned {self.total_score} points")
                        print(f"Total score is {self.total_score} points")

                        rollagain = 0
                    elif decision == "r":
                        rollagain = 1
                        if Dices == 0:
                            Dices = 6
                        continue

                    # check forf the quitter decision
                    if decision == "q":
                        if self.round > 1 or self.banker.shelved != 0:
                            #print(f"Total score is {self.total_score} points")
                            print(f"Thanks for playing. You earned {self.total_score} points")
                        break
                    self.round += 1


if __name__ == "__main__":
    from game_logic import GameLogic
    from banker import Banker
    game = Game(GameLogic.roll_dice)
    game.play()