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
    plt.show()

def avg_pie(self):
    """Creates a new dataframe and a pie graph for the average of each item type 
    given in the data. 
        
    Returns:
        A new dataframe and pie chart for the average percentage spent 
        on each item type.
    """
    avg = self.purchase_data.groupby("Item type")["Cost"].mean()
    pie_graph = avg.plot(
    kind='pie', autopct='%1.1f%%', explode=(0.1, 0.1, 0.1, 0.1),
    title='Average Percentage Spent Per Item Type',
    figsize=(7,7),
    startangle=90
    )
    plt.show()