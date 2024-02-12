import matplotlib.pyplot as plt
import pandas as pd
mydata=pd.read_csv('firstdDataScience/Share slim (1).csv')
(mydata)
Name_data=mydata["name"]
Age_data=mydata["age"]
City_data=mydata["city"]
Salary_data=mydata["salary"]
plt.plot(Name_data,City_data, color='r',label='city')
plt.plot()
plt.xlabel('Names')
plt.ylabel('city')
plt.title(' PERSONNEL CONFIDENTIAL DETAILS ')
plt.legend()
plt.show()