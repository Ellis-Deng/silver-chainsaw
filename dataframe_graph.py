"""This is a possible way to turn a CSV file into a dataframe and then create 
a time series graph. Also, creating a new dataset for the average amount that
an individual spends on a specific item."""

import pandas as pd

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
        purchase_data (dataset): a dataset of all purchases 
    """