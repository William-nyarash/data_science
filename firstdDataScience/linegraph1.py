#LINE GRAPHS:
#Visualization Code:
import matplotlib.pyplot as plt
import pandas as pd

#data title
mydata = pd.read_csv('firstdDataScience/Share slim (1).csvgit ')
country_data = mydata["name"]
medal_data = mydata["gold"]
plt.plot(country_data, medal_data, label="Distribution",color='b')
plt.plot()
plt.xlabel("country_data")
plt.ylabel("medal_data")
plt.title("Gold medal achievements of five most successful\n"+"countries in 2023 Summer Olympics")