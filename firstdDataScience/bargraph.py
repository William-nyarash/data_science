#BAR CHARTS:
#Visualization Code:
import matplotlib.pyplot as plt

import pandas as pd

mydata = pd.read_csv('firstdDataScience/Share slim (1).csv')
country_data = mydata["name"]
medal_data = mydata["gold"]
plt.bar(country_data, medal_data, label="AWARD", color='#865252')
plt.plot()
plt.xlabel("country_data")
plt.ylabel("medal_data")
plt.title("Gold medal achievements of five most successful\n"+"countries in 2023 Summer Olympics")
plt.legend()
plt.show()