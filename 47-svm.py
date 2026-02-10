    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV


cancer = load_breast_cancer()
print(cancer.keys())
print(cancer['DESCR'])
print(cancer['target_names'])

df_features = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
print(df_features.head())
X = df_features
y = cancer['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
model = SVC()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(confusion_matrix(y_test, predictions))
print('\n')
print(classification_report(y_test, predictions))

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001]}
grid = GridSearchCV=GridSearchCV(SVC(), param_grid, verbose=3)
grid.fit(X_train, y_train)
grid.predictions = grid.predict(X_test)
print(confusion_matrix(y_test, grid.predictions))
print('\n') 
print(classification_report(y_test, grid.predictions))
