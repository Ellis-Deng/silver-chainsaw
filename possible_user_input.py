import pandas as pd
"""A possible way to record user input on their spendings"""

class Spendings:
    """Records a user's spendings
    
    
    Attributes:
        total (int): the total amount that a user spend in a given amount of 
        time        
        
        num_purchases (int): the amount of purchases a user makes
        
        expense_info (dictionary): a dictionary where the keys are the 
        date of the purchase and the values are the items bought and the 
        price paid for them
        
    """
    def __init__(self, date, item_type, item, cost):
        """Initializes values
        
        Args: 
            num_purchases(int): the number of purchases a user has made
            budget(int): the amount of money a user is permitted to spend
        
        Side effects:
            initializes values"""
        
        self.date = date
        self.item_type = item_type
        self.item = item    
        self.cost = cost
    
    def purchases(self):
        """Creates a dictionary of purchases
        
        Returns:
            dictionary: a representation of all the purchases made
            
        Side effects:
            Prints to console"""
        return 0
    
    def file_commit(self, commit, file):
        """Initializes values
        
        Args: 
            commit(boolean): whether or not the purchases want to be added to
            a file
            
            file(string): a string containing a path to a file that the user
            has the option to write to
        
        Side effects:
            Writes data to a file"""
        
        self.commit = commit
        with open(file,"w",encoding="utf-8") as f:
            if self.commit == True:
                f.write(self.expense_info)



num_purchases = int(input("How many purchases did you make: "))
budget = int(input("What is your budget: "))
for x in range(num_purchases):
    expense = input("What expense did you spend money on: ")
    amount = float(input("How much did you spend: "))
    expense_object = Spendings(amount, expense, num_purchases, budget)
    expense_object.purchases()


commit = input("Would you like to commit to a file: ")
