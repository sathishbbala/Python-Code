import seaborn as sns
import matplotlib.pyplot as plt

# tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# print(tips.head())
print(flights.head())

# sns.displot(tips['total_bill'])
# sns.jointplot(x='total_bill', y='tip', data = tips)
# sns.pairplot(tips)
# sns.barplot(x='sex', y='tip', data=tips)
# sns.boxplot(x='day', y='total_bill', data=tips)
# sns.boxplot(x='day', y='total_bill', data=tips, hue='sex')
pt = flights.pivot_table(index='month', columns='year', values='passengers')
print(pt)
sns.heatmap(pt, cmap='coolwarm', linecolor='white', linewidths=1)
plt.show()