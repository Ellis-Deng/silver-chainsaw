import pandas as pd
"""A possible way to record user input on their spendings"""

class Spendings:
    """Records a user's spendings
    
    
    Attributes:
        cost (list): 
            a list of the cost of the items that a user buys
        
        item_type (int): 
            a list of the types of items a user spends their money on
        
        item (list): 
            a list of the specific items a user buys
        
        date (list): 
            a list of the dates that a user made their purchases
        
    """
    def __init__(self, cost, item_type, item, date):
        """Initializes values
        
        Args: 
            cost (list): 
                a list of the cost of the items that a user buys
        
            item_type (int): 
                a list of the types of items a user spends their money on
            
            item (list): 
                a list of the specific items a user buys
            
            date (list): 
                a list of the dates that a user made their purchases
        
        Side effects:
            initializes values"""
        self.item_type = list(item_type)
        self.item = list(item)
        self.cost = list(cost)
        self.date = list(date)
        
    def create_df(self):
        """Creates a dataframe of purchases
        
        Returns:
            df: a dataframe of all the purchases made
            """
            
        data = {'Date': self.date,'Item Type': self.item_type, 
                'Item': self.item, 'Cost': self.cost}
        df = pd.DataFrame(data)
        self.df = df
        return(df.to_string(index=False))
    
    def file_commit(self, commit, file):
        """Sends the user created df to a .csv file
        
        Args: 
            commit(boolean): whether or not the purchases want to be added to
            a file
            
            file(string): a string containing a path to a file that the user
            has the option to write to
        
        Side effects:
            Writes data to a file"""
        dframe = pd.read_csv(open(file))
        #print(dframe)
        if commit == True:
            self.df.to_csv(file, mode='a', header=False, index=False)
            print(dframe)
            

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
    print(user_data.create_df())
print(f"You have made {counter} purchases overall")
if counter > 0:
    commit = input("Would you like to commit to a file: ")
    if commit == 'y':
        user_data.file_commit(True,"sample_data.csv")
    else:
            print("Thank you for using the program!")
