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
    def __init__(self, num_purchases, budget = None):
        """Initializes values
        
        Args: 
            num_purchases(int): the number of purchases a user has made
            budget(int): the amount of money a user is permitted to spend
        
        Side effects:
            initializes values"""
        
        self.budget = budget
        self.num_purchases = num_purchases
    
    def purchases(self):
        """Creates a dictionary of purchases
        
        Returns:
            dictionary: a representation of all the purchases made
            
        Raises:
            TypeError: The amount spent was not a float
            
        Side effects:
            Expects input from the user
            Prints to console"""
        expense_info = {}
        for x in range(self.num_purchases):
            expense = input("What expense did you spend money on: ")
            amount = float(input("How much did you spend: "))
            if isinstance(amount,float) == False:
                raise TypeError
            total_spent = amount + total_spent
            if (total_spent > self.budget):
                print("You are out of money, no more purchases can be made")                
            date = input("What date did you spend this on: ")
            expense_info[date] = amount, expense
        self.expense_info = expense_info
        return(self.expense_info)
    
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
        
        
    
