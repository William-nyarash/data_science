#Visualization Code:
import matplotlib.pyplot as plt
import pandas as pd
mydata = pd.read_csv('firstdDataScience/Share slim (1).csv')
country_data = mydata["name"]
medal_data = mydata["gold"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2023 Summer Olympics")
plt.show()