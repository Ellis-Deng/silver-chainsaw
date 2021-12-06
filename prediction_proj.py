"""Opens the text file created by Ajay, scrapes the numbers from the dictionary, and adds 
them up, divides this number by the number of days to get an average amount spent over the week. 
Then, the program takes this number,  and adds the amount of an extra/bonus item that is randomly generated. 
Then, the program determines if this additional item is a bad idea or not."""

def average(file, folder):
    """This function scrapes data and makes an average budget for weeks, which is then used by the following functions as well.
    It reads the daily spendatures, then compiles them into an average budget to be used later. 
    
    Args: the file, preferably in text format, and the folder where the data comes from.
    
    Returns: average cost"""
    
    with open (file, "r", encoding = "utf-8") as f: 
        total_sum = 0
        count = 0
        for line in f:
            week = line.split(",")
            for number in week:
                count = count + 1
                total_sum = total_sum + int(number)
        return total_sum/count
          
def determine(price, max, file, folder):
    """This function determines if the additional item added to the average cost would go over 
    the maximum budget alloted by the program and user. The average cost is determined from the average() function
    
    Args: the max budget decided by the user, and the avg cost, which is determined by the average() function, and an item(?) 
    that the user wishes to add onto the total. If the item brings the total over, then 
    
    Returns: a statement that declares whether or not """
    
    """cost = 0 but will be updated each time there is a new item with a different price"""
    avg = average(file, folder)
    if (avg + price < max):
        return False
    else:
        return True