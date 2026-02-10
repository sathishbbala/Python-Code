import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())

pairplot = sns.pairplot(iris, hue='species', palette='Dark2')
plt.show()