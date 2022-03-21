class Banker:
    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, shelved_points):
        """
        A method used to store the points in each roll
        INPUT: Integer that represents the points to be added to the shelf
        OUTPUT: Temporary store unbanked points
        """
        self.shelved += shelved_points
        return self.shelved

    def bank(self):
        """
        A method that is used to add the points gained in the roll to the total, and reset the shelf to zero
        INPUT: Nothing
        OUTPUT: Amount of points added to total from shelf
        """
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        """
        A method used to clear all unbanked points
        INPUT: Nothing
        OUTPUT:
        """
        self.shelved = 0
