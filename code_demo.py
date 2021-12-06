import pandas as pd
import matplotlib.pyplot as plt

#creating the dataframe and showing it
purchase_data = pd.read_csv("sample_data.csv")
print(purchase_data)

#Plotting a line graph
purchase_data.plot(kind = 'line',
                        x = 'Date',
                        y = 'Cost',
                        color = 'blue',
                        marker = 'o')
plt.title('Purchases Over Time')
plt.xlabel('Date')
plt.ylabel('Cost in $')
plt.grid(True)
plt.show()

#Plotting a Pie Chart for average cost by Item type
avg = purchase_data.groupby("Item type")["Cost"].mean()
print(avg)
pie_graph = avg.plot(
    kind='pie', autopct='%1.1f%%', explode=(0.1, 0.1, 0.1, 0.1),
    title='Average Percentage Spent Per Item Type',
    figsize=(7,7),
    startangle=90
    )
plt.show()