"""This is a possible way to turn a CSV file into a dataframe and then create 
a time series graph for the data. Also, creating a new dataset for the average 
amount that an individual spends on a specific item."""

import pandas as pd
import matplotlib.pyplot as plt

def open_file(self, purchase_data):
    """Opens a CSV file and turns it into a dataframe.

    Args:cl
        purchase_data: the name of the dataframe that the data is going to be
        stored into. 
        
    Returns:
        A dataframe for the inputed CSV file.
    """
    self.purchase_data = purchase_data
    purchase_data = pd.read_csv("sample_data.csv")
    return purchase_data

def graph(self):
    """Creates a graph based off of the given data. 

    Args:
        purchase_data (dataset): a dataframe of all purchases.
        
    Returns:
        A time series graph for all purchases that have been made. 
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
    return plt.show()

def average_dataframe(self):
    """Creates a new dataframe for the average of each item given in the data. 

    Args:
        purchase_data (DataFrame): a dataframe of all purchases.
        
    Returns:
        A new dataframe that contains the average amount of money spent on each
    """
    columns = self.purchase_data["Item", "Cost"]
    item_price = self.purchase_data[columns]
    avg_price = item_price.groupby("Item")["Cost"].mean()
    pie_chart = avg_price.plot.pie(y='Cost', figsize=(5,5))
    print(pie_chart)
    return avg_price    