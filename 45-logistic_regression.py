import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf

train  = pd.read_csv('data/titanic_train.csv')
print(train.head())

# Find which data is missing 
print(train.isnull()) # False indicates missing data

# Build a heatmap to visualize missing data
# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')

sns.set_style('whitegrid')
# Exploratory Data Analysis
# sns.countplot(x='Survived', data=train, hue='Sex') # shows the survival rate based on gender
# sns.countplot(x='Survived', data=train, hue='Pclass') # shows the survival rate based on passenger class
# sns.displot(train['Age'].dropna(), bins=30) # histogram of age distribution
# train['Age'].hist(bins=30) # pandas visualization showing the histogram of age
# sns.countplot(x='SibSp', data=train) # shows the count of siblings/spouses aboard
# train['Fare'].hist(bins=40, figsize=(10,4)) # histogram of fare distribution
# use cufflinks for interactive plots
cf.go_offline()
# train['Fare'].iplot(kind='hist', bins=30, color=(255,0,0)) # interactive histogram of fare distribution - did not work gave an error about color 
sns.boxplot(x='Pclass', y='Age', data=train) # boxplot showing age distribution across passenger classes

plt.show()