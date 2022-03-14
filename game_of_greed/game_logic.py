class GameLogic:
    def __init__(self):
        pass

    def calculate_score(roll):
        occurance = []
        threes = []

        for no in roll:
            occurance.append(0)

        for no in roll:
            occurance[no - 1] = int(occurance[no - 1]) + 1

        for no in occurance:
            if no >= 3:
                threes.append(no)
            else:
                threes.append(0)

        if set(roll) == set([1, 2, 3, 4, 5, 6]):
            return 1000

        elif len(roll) == 6 and len(set(roll)) == 3 and set(occurance) == set([0, 2]):
            return 1000

        elif roll == [1, 1, 1, 1, 1, 1]:
            return 1000000

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

        elif 1 in roll or 5 in roll:
            total = 0
            total = total + (len(list(filter(lambda no: no == 1, roll))) * 100)
            total = total + (len(list(filter(lambda no: no == 5, roll))) * 50)
            return total

        else:
            return 0

    def roll_dice(dices):
        pass


class Banker:
    total = 0

    def __init__(self):
        pass

    def shelf(temPoint):
        pass

    def bank(unbanked):
        pass

    def clear_shelf():
        pass
