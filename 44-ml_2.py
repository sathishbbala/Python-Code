# Linear Regression example program using Ecommerce Customers dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

customers = pd.read_csv('data/Ecommerce Customers')
# print(customers.columns.tolist())

# print(customers.head())
# print(customers.describe())

# sns.jointplot(data=customers, x='Time on Website', y='Yearly Amount Spent') #shows the correlation between the Time on website and yearly amount spent
# sns.jointplot(data=customers, x='Time on App', y='Yearly Amount Spent')
# sns.pairplot(data=customers)

y = customers['Yearly Amount Spent'] # predict what the yearly amount spent will be 
X = customers[['Avg. Session Length','Time on App','Time on Website','Length of Membership']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.coef_) # coefficients of the model 

predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
plt.xlabel('Y Test (True Values)')
plt.ylabel('Predicted Values')

print(metrics.mean_absolute_error(y_test, predictions))
print(metrics.mean_squared_error(y_test, predictions))
print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))

sns.displot((y_test-predictions), bins=50)

plt.show()