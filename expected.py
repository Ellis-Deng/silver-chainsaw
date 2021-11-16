import pandas as pd 
from random import choices

def expected_expense(csvfile):
    """
    The purpose of this method will be to predict the next expense 
    a person will make depending on the already known expenses by using 
    probabilities and random generator
    
    Args:
        csvfile: file containing all the data on the person's expenses 
    """

    df=pd.read_csv(csvfile, index_col=0)
    probabilities=df["item_name"].value_counts(normalize=True)
    expected_item=choices(probabilities,weights=probabilities,k=1)
    return expected_item
    
    
    