
class Game:
    def __init__(self, roller = None):
        self.roller = roller
        self.banker = Banker()
        self.game_logic = GameLogic()
    def play(self):
        print("Welcome to Game of Greed")
        wanna_play = input("Wanna play? ")
        if wanna_play == "n":
            print("OK. Maybe another time")
        else:
            round = 1
            banked = self.banker.bank()
            print(f'Starting round {round}')
            while (round <= 6):
                print("Rolling 6 dice...")
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))
                decision = input("Enter dice to keep (no spaces), or (q)uit: ")
                if (decision == "q"):
                    if (round > 1):
                        print(f'Total score is {banked} points')
                    print(f'Thanks for playing. You earned {banked} points')
                    break
                else:
                    decisionList = list(map(int, str(decision)))
                    unpacked = self.game_logic.calculate_score(decisionList)
                    shelf = self.banker.shelf(unpacked)
                    banked = self.banker.bank()
                    print(f'You have {banked} unbanked points and {6-len(decisionList)} dice remaining')
                    decisionBankedPoint = input("(r)oll again, (b)ank your points or (q)uit ")
                    if decisionBankedPoint == "b":
                        print(f'You banked {banked} points in round {round}')
                        print(f'Total score is {banked} points')
                        print(f'Starting round {round + 1}')
                    elif decisionBankedPoint == "r":
                        continue
                round += 1

if __name__ == "__main__":
    from game_logic import GameLogic, Banker
    game = Game(GameLogic.roll_dice)
    game.play()