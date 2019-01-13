import pandas
import matplotlib.pyplot as plt

df=pandas.read_csv('gapminder.tsv', sep='\t')
print(df.head())


x=[2015, 2016, 2017, 2018]
y=[100, 200, 300, 400]
plt.plot(x,y)
plt.show()
