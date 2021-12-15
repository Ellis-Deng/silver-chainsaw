import pandas as pd
import matplotlib.pyplot as plt

class Graph:
    def open_file(self, purchase_data):
        """Opens a CSV file and turns it into a dataframe.

    Args:
        purchase_data: the name of the dataframe that the data is going to be
        stored into. 
        
    Returns:
        A dataframe for the inputed CSV file.
    """
        purchase_data = pd.read_csv("sample_data.csv")
        self.purchase_data = purchase_data
        print(purchase_data)
        return purchase_data

    def graph(self):
        """Creates a time series graph based off of the given data. 

        Args:
            purchase_data (dataset): a dataframe of all purchases.
            
        Returns:
            A time series graph for all purchases that have been made. 
            
        Source:
            I had used information from pandas.pydata.org to help develop the 
            code for the time series graph below. The main thing that I had used 
            from the website was the general layout of plot() because at the time 
            of  creating this code I had no idea how to use plot(). 
        """
        self.purchase_data.plot(kind = 'line',
                            x = 'Date',
                            y = 'Cost',
                            color = 'blue',
                            marker = 'o')
        plt.title('Purchases Over Time')
        plt.xlabel('Date')
        plt.ylabel('Cost in $')
        plt.grid(True)
        plt.show()
        
    def avg_pie(self):
        """Creates a new dataframe and a pie graph for the average of each item type 
        given in the data. 
            
        Returns:
            A new dataframe and pie chart for the average percentage spent 
            on each item type.
            
        Source:
            I had used information from pandas.pydata.org to help develop the 
            code for the pie graph below. Since I had the general structure from
            the graph method, all I had to do was set the kind=pie. However, for
            the other parameters such as autopct and explode, I had used 
            matplotlib.org to set those up. The reason I wanted those two 
            parameters in the pie chart are to display the percentages on each
            slice and create a more visually appealing pie chart with the 
            explode parameter. 
        """
        avg = self.purchase_data.groupby("Item type")["Cost"].mean()
        pie_graph = avg.plot(
            kind='pie', autopct='%1.1f%%', explode=(0.1, 0.1, 0.1, 0.1),
            title='Average Percentage Spent Per Item Type',
            figsize=(7,7),
            startangle=90)
        plt.show(pie_graph)
        
class Spending:
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
            
        Side effects:
            creates self.df, which is initialized here and used in other methods
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
        if commit == True:
            self.df.to_csv(file, mode='a', header=False, index=False)
            

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
    item_type = input("What kind of item did you buy (Food, Other, Utilities,"
                      +" or Personal): ")
    item_type_list.append(item_type)
    item = input("What item did you buy: ")
    item_list.append(item)
    date = input("On what date did you make the purchase: ")
    date_list.append(date)
    counter+=1
    user_data = Spending(cost_list, item_type_list, item_list, date_list)
    print(user_data.create_df())
if counter == 1:
    print(f"You have made {counter} purchase overall")
else:
    print(f"You have made {counter} purchases overall")
if counter > 0:
    commit = input("Would you like to commit to a file: ")
    if commit == 'y':
        user_data.file_commit(True,"sample_data.csv")
        graphing = Graph()
        graphing.open_file("sample_data.csv")
        graphing.graph()
        graphing.avg_pie()
        
print("Thank you for using the program!")
