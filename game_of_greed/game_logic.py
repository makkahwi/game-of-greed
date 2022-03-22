import random


class GameLogic:
    def __init__(self):
        pass

    def calculate_score(input, sec=False):
        """
        A method that returns the roll's score based on the rules of the game.
        INPUT: Tuple of integers that represent a dice roll
        OUTPUT: Integer representing the roll's score
        """

        # Create new array #######################################################################
        roll = []

        for x in input:
            roll.append(x)

        # Check if the roll is a sequence of 1 to 6 ##############################################
        if set(roll) == set([1, 2, 3, 4, 5, 6]):
            return 1500

        total = 0

        # This is to identify how many occurrences there are of each of the numbers ##############
        occurance = [0, 0, 0, 0, 0, 0]

        for no in roll:
            occurance[no - 1] = int(occurance[no - 1]) + 1

        # Check if the roll has 3 pairs ##########################################################
        if len(roll) == 6 and len(set(roll)) == 3 and set(occurance) == set([0, 2]):
            return 1500

        # Check if the roll has occurrences of three or more #####################################
        if len(list(filter(lambda no: no >= 3, occurance))) > 0:
            i = 1

            for no in occurance:
                # Check if one has three occurrences
                if i == 1 and no == 3:
                    total = total + 1000
                    roll = list(filter(lambda num: num != i, roll))
                # Check if one has four occurrences
                elif i == 1 and no == 4:
                    total = total + 2000
                    roll = list(filter(lambda num: num != i, roll))
                # Check if one has five occurrences
                elif i == 1 and no == 5:
                    total = total + 3000
                    roll = list(filter(lambda num: num != i, roll))
                # Check if one has six occurrences
                elif i == 1 and no == 6:
                    return 4000
                # Check if any other number has three occurrences
                elif no == 3:
                    total = total + i * 100
                    roll = list(filter(lambda num: num != i, roll))
                # Check if any other number has four occurrences
                elif no == 4:
                    total = total + i * 200
                    roll = list(filter(lambda num: num != i, roll))
                # Check if any other number has five occurrences
                elif no == 5:
                    total = total + i * 300
                    roll = list(filter(lambda num: num != i, roll))
                # Check if any other number has six occurrences
                elif no == 6:
                    return i * 400

                i = i + 1

        # Check if the roll has any fives or ones ################################################
        if 1 in roll or 5 in roll:
            total = total + (len(list(filter(lambda no: no == 1, roll))) * 100)
            total = total + (len(list(filter(lambda no: no == 5, roll))) * 50)

        # Return total ###########################################################################
        return total

    @staticmethod
    def roll_dice(dices):
        """
        A method that returns a tuple of integers representing the dice roll
        INPUT: Integer between 1 and 6
        OUTPUT: Tuple of random values between 1 and 6
        """
        random_list_values = []
        for _ in range(1, dices + 1):
            random_int = random.randint(1, dices)
            random_list_values.append(random_int)

        random_values = tuple(random_list_values)

        return random_values

