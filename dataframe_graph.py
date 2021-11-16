"""This is a possible way to turn a CSV file into a dataframe and then create 
a time series graph for the data. Also, creating a new dataset for the average 
amount that an individual spends on a specific item."""

import pandas as pd
import matplotlib.pyplot as plt

def open_file(fpath, folder):
    """Opens a CSV file and turns it into a dataframe.

    Args:
        fpath: a file path for the given data.
        folder: a folder that contains the data. 
        
    Returns:
        A dataframe for the inputed CSV file.
    """
    fpath = f'{folder}/money-spent.csv'
    purchase_data = pd.read_csv(fpath)
    return purchase_data

def graph(purchase_data):
    """Creates a graph based off of the given data. 

    Args:
        purchase_data (dataset): a dataset of all purchases.
        
    Returns:
        A time series graph for all purchases that have been made. 
    """
    purchase_data.plot(kind = 'line',
                        x = 'date',
                        y = 'price',
                        color = 'red')
    plt.title('Purchases')
    return plt.show()

def average(purchase_data):
    """

    Args:
        purchase_data ([type]): [description]
    """
