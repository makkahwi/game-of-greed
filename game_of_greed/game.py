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
        # Welcoming #######################################################################
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")

        # Wanna Play Cases ################################################################
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            round = 1
            banked = self.banker.bank()
            print(f"Starting round {round}")

            while round <= 6:
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(",".join(nums))

                # User Response to rolling result ##################################
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")

                # Quit Case ########################################################
                if decision == "q":
                    if round > 1:
                        print(f"Total score is {banked} points")
                    print(f"Thanks for playing. You earned {banked} points")
                    break

                # Putting a side dices case ########################################
                else:
                    decisionList = list(map(int, str(decision)))
                    unpacked = GameLogic.calculate_score(decisionList)
                    shelf = self.banker.shelf(unpacked)
                    banked = self.banker.bank()

                    # Roll, bank or quit cases #####################################
                    print(
                        f"You have {banked} unbanked points and {6-len(decisionList)} dice remaining"
                    )
                    decisionBankedPoint = input(
                        "(r)oll again, (b)ank your points or (q)uit "
                    )

                    # Bank case ####################################################
                    if decisionBankedPoint == "b":
                        print(f"You banked {banked} points in round {round}")
                        print(f"Total score is {banked} points")
                        print(f"Starting round {round + 1}")

                    # Roll case ####################################################
                    elif decisionBankedPoint == "r":
                        continue
                round += 1


if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
