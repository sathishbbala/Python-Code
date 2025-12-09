
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df = pd.read_csv('data/USA_Housing.csv')
print(df.head())

# sns.displot(df['Price'])
# print(df.corr(numeric_only=True))
# sns.heatmap(df.corr(numeric_only=True))

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)

cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coeff'])
print(cdf)

# Moving to Predictions 
predictions = lm.predict(X_test)
print(predictions)
plt.scatter(y_test, predictions)

# In a regression problem, ML Model predicts a number
# Predictions are never perfect 
# So how far are the predictions from the actual values?
# It is measured as a loss (during training) and error (during evaluation)
# MAE - Mean Absolute Error = average of absolute differences between predictions and real values 
# How wrong was the prediction on average 
# mean_squared_error
# Root mean squared error 
print(metrics.mean_absolute_error(y_test, predictions))
print(metrics.mean_squared_error(y_test, predictions))
print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
plt.show()