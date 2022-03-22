from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic

class Game:
    def __init__(self, roller=None):
        self.roller = roller

    def play(self):
        """
        A method that interacts with user inputs. Limited to only given cases of user interaction.
        Soon to be enhanced to deal with more scenarios of user play inputs.
        """
        # Welcoming msg
        print("Welcome to Game of Greed")
        # To start the game, either the player enters (y or n)
        want_to_play = input("Wanna play? ")
        # User doesn't want to play
        if want_to_play == "n":
            print("OK. Maybe another time")
        # User wants to play
        else:
            banker = Banker()
            round = 1
            print(f"Starting round {round}")
            while True:
                num_of_dices = 6
                print(f"Rolling {num_of_dices} dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(",".join(nums)) 
                score = GameLogic.calculate_score(list(map(int,nums)))  
                if score == 0:
                    print("Zilch!!! Round over")
                    print(f"You banked {banker.shelved} points in round {round}")
                    break
                # Get input from the player (available in the rolled dice, not available, quit)           
                first_decision = input("Enter dice to keep (no spaces), or (q)uit: ") 
                # Player doesn't want to quit
                if first_decision != "q":
                    decisionList = list(map(int, str(first_decision)))
                    num_of_dices = num_of_dices - len(decisionList)
                    rolled_dice = list(map(int,nums))
                    is_cheating = False
                    for i in decisionList:
                        if i not in rolled_dice or decisionList.count(i) > rolled_dice.count(i):
                            is_cheating = True
                            print("Cheater!!! Or possibly made a typo...")
                            print(",".join(nums))
                            first_decision = input("Enter dice to keep (no spaces), or (q)uit: ") 
                            decisionList = list(map(int, str(first_decision)))
                        if i in rolled_dice or decisionList.count(i) < rolled_dice.count(i):
                            # Calculate score if decision list is in rolled_dice      
                            score = GameLogic.calculate_score(decisionList)
                            banker.shelf(score)
                            print(f"You have {banker.shelved} unbanked points and {6 - len(decisionList)} dice remaining")
                            # Get the input from the player to bank points, roll again or quit
                            second_decision = input("(r)oll again, (b)ank your points or (q)uit ")
                            # Player doesn't want to quit but the total score is not zero
                            if score != 0 and second_decision == "q":
                                print(f"Total score is {banker.balance} points")
                                print(f"Thanks for playing. You earned {banker.balance} points")
                                break
                            # Player wants to bank points
                            if second_decision == "b":   
                                print(f"You banked {banker.shelved} points in round {round}")
                                banker.bank()
                                print(f"Total score is {banker.balance} points")
                                round += 1
                                print(f"Starting round {round}")
                            # Player wants to roll again 
                            elif second_decision == "r":
                                #
                                # print(f"Rolling {num_of_dices} dice...")
                                break
                            continue
                    break
                # Player wants to quit and the total score is equal to zero
                else:
                    if score == 0:
                        print(f"Total score is {banker.balance} points")
                    print(f"Thanks for playing. You earned {banker.balance} points")
                    break


if __name__ == "__main__":
    from game_logic import GameLogic
    from banker import Banker
    game = Game(GameLogic.roll_dice)
    game.play()