from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:
    def __init__(self, roller=None):
        self.roller = roller
        self.banker = Banker()

    def play(self):
        """
        A method that interacts with user inputs. Limited to only given cases of user interaction.
        Soon to be enhanced to deal with more scenarios of user play inputs.
        """
        print("Welcome to Game of Greed")
        want_to_play = input("Wanna play? ")
        if want_to_play == "n":
            print("OK. Maybe another time")
        else:
            round = 1
            print(f"Starting round {round}")
            while True:
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(",".join(nums))
                first_decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if first_decision == "q":
                    total_score = self.banker.bank()
                    if total_score != 0:
                        print(f"Total score is {total_score} points")
                        print(f"Thanks for playing. You earned {total_score} points")
                    else:
                        print(f"Thanks for playing. You earned {total_score} points")
                    break
                else:
                    decisionList = tuple(map(int, str(first_decision)))
                    score = GameLogic.calculate_score(decisionList)
                    unbanked_points = self.banker.shelf(score)
                    print(
                        f"You have {unbanked_points} unbanked points and {6 - len(decisionList)} dice remaining"
                    )
                    second_decision = input(
                        "(r)oll again, (b)ank your points or (q)uit "
                    )
                    if second_decision == "b":
                        total_score = self.banker.bank()
                        print(f"You banked {unbanked_points} points in round {round}")
                        print(f"Total score is {total_score} points")
                        round += 1
                        print(f"Starting round {round}")
                    else:
                        continue


if __name__ == "__main__":
    from game_logic import GameLogic
    from banker import Banker

    game = Game(GameLogic.roll_dice)
    game.play()
