import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())
# sns.displot(tips['total_bill'])
# sns.jointplot(x='total_bill', y='tip', data = tips)
sns.pairplot(tips)

plt.show()