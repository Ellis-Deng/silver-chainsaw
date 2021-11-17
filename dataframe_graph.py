"""This is a possible way to turn a CSV file into a dataframe and then create 
a time series graph for the data. Also, creating a new dataset for the average 
amount that an individual spends on a specific item."""

import pandas as pd
import matplotlib.pyplot as plt

def open_file(purchase_data):
    """Opens a CSV file and turns it into a dataframe.

    Args:
        purchase_data: the name of the dataframe that the data is going to be
        stored into. 
        
    Returns:
        A dataframe for the inputed CSV file.
    """
    purchase_data = pd.read_csv("money-spent.csv")
    return purchase_data

def graph(purchase_data):
    """Creates a graph based off of the given data. 

    Args:
        purchase_data (dataset): a dataframe of all purchases.
        
    Returns:
        A time series graph for all purchases that have been made. 
    """
    purchase_data.plot(kind = 'line',
                        x = 'date',
                        y = 'price',
                        color = 'red')
    plt.title('Purchases Over Time')
    return plt.show()

def average_dataframe(purchase_data):
    """Creates a new dataframe for the average of each item given in the data. 

    Args:
        purchase_data (DataFrame): a dataframe of all purchases.
        
    Returns:
        A new dataframe that contains the average amount of money spent on each
    """
    columns = purchase_data["item", "price"]
    item_price = purchase_data[columns]
    avg_price = item_price.groupby("item")["price"].mean()
    return avg_price
    