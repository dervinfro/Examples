#!/usr/bin/env python3

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsRegressor # fifth question
from sklearn.pipeline import make_pipeline # fifth question
from sklearn.preprocessing import StandardScaler # fifth question
from sklearn.model_selection import cross_val_score # fifth question

pd.options.display.max_columns=None
pd.options.display.max_rows=None
pd.options.display.width=135
#pd.options.display.float_format='{:.3f}'.format

df = pd.read_csv('/Users/user/Downloads/ML Analytics/ML Analytics - Course 3/quiz2data.csv')

# As per the instructions, the dependent variable is log of value
df['log_value'] = np.log(df['value'])

#we need a constant variable in OLS models (SEE: https://www.theanalysisfactor.com/the-impact-of-removing-the-constant-from-a-regression-model-the-categorical-case/)
df['const'] = 1

X = df[['const','elem_score','homeowner']]
y = df['log_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=25)
print(X_train, sep='\n')
print(X_train.T, sep='\n') # a Transpose of X_train.  Turns of columns of X_train into rows and TRANSPOSES the values.
print(X_train.T.iloc[0:3,0:6]) # output transposed rows (0-2) and prints the transposed columns (0-5)


