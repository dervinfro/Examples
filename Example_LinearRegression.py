#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 23:26:34 2021

@author: user
https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
"""
#%% Intro Section
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df = pd.read_csv('/Users/user/Downloads/Python Airdroped 13MAY2020/student_scores.csv')

#%% Section 1
# Columns
columns = df.columns

# Shape of dataframe
shape = df.shape

# Top 5 rows
head = df.head(10)

# Dataframe statistics
describe = df.describe()

#%% Section 2
df.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs. Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Precentage Score')

#%% Section 3
X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Set the regressor object
regressor = LinearRegression()

# Call the fit method 
regressor.fit(X_train, y_train)

# Print out the line intercept value: 2.018160041434662
print("Regressor line intercept: ", regressor.intercept_)

# Print out the coefficient: [9.91065648]
# This means that for every Hour increased, the Score goes up [9.91065648]
print("Regressor Coefficient: ", regressor.coef_)

# Find out the predicted values using X_test
y_pred = regressor.predict(X_test)

# Set the new df to compare Actual versus Predicted
df_new = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))





