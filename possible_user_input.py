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
    def __init__(self, cost, item_type, item, date):
        """Initializes values
        
        Args: 
            num_purchases(int): the number of purchases a user has made
            budget(int): the amount of money a user is permitted to spend
        
        Side effects:
            initializes values"""
        self.item_type = list(item_type)
        self.item = list(item)
        self.cost = list(cost)
        self.date = list(date)
    def sort(self):
        """Creates a dictionary of purchases
        
        Returns:
            dictionary: a representation of all the purchases made
            
        Side effects:
            Prints to console"""
        data = {'Item Type': self.item_type, 'Item': self.item, 'Cost': self.cost}
        df = pd.DataFrame(data, index=self.date)
        return(df)
    
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

date_list = []
item_type_list = []
item_list = []
cost_list = []
counter = 0
print("Welcome to the input for your purchases. If you wish to stop making " + 
      "purchases at any time, you can enter 0 for the cost of the item.")
while True:
    cost = float(input("How much did your item cost: "))
    if cost == 0:
        break
    cost_list.append(cost)
    item_type = input("What kind of item did you buy: ")
    item_type_list.append(item_type)
    item = input("What item did you buy: ")
    item_list.append(item)
    date = input("On what date did you make the purchase: ")
    date_list.append(date)
    counter+=1
user_data = Spendings(cost_list, item_type_list, item_list, date_list)
print(user_data.sort())
print(f"You have made {counter} purchases")
if counter > 0:
    commit = input("Would you like to commit to a file: ")
