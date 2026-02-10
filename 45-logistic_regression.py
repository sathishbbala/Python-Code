# Logistic Regression on Titanic Dataset
# This script performs data analysis and preprocessing on the Titanic dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
    

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
# cf.go_offline()
# train['Fare'].iplot(kind='hist', bins=30, color=(255,0,0)) # interactive histogram of fare distribution - did not work gave an error about color 
# sns.boxplot(x='Pclass', y='Age', data=train) # boxplot showing age distribution across passenger classes

# Cleaning the data
train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)   # populate age column with mean age based on passenger class
train.drop('Cabin', axis=1, inplace=True) # drop cabin column due to too many missing values
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis') 
train.dropna(inplace=True) # drop any remaining rows with missing data

sex = pd.get_dummies(train['Sex'], drop_first=True) # convert categorical gender data to numerical
print(sex.head())
embark = pd.get_dummies(train['Embarked'], drop_first=True) # convert categorical embarked data to numerical
print(embark.head())    
train = pd.concat([train, sex, embark], axis=1) # concatenate new dummy columns to the original dataframe
train.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True) # drop original categorical columns and unnecessary columns    
train.drop('PassengerId', axis=1, inplace=True) # drop PassengerId column as it is not needed for analysis
print(train.head()) 

plt.show()