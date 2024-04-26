import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('age_and_income.csv')
print(dataframe.head())

# Create Scatter Plot
dataframe.plot.scatter(x='Age', y='Income($)', title='Age vs Income')
plt.show()

# Create Bar Chart
dataframe.sort_values(by='Age', ascending=True, inplace=True)
dataframe.plot.bar(x='Age', y='Income($)', title='Age vs Income')

plt.show()
