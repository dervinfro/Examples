#!/usr/bin/env python3

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


#pd.options.display.float_format='{:.3f}'.format
np.set_printoptions(suppress=True) #suppresses scientific notation
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('/Users/user/Downloads/ML Analytics/ML Analytics - Course 3/quiz2data.csv')	

df['log_value'] = np.log(df['value'])

df['const'] = 1

X = df[['const','medhinc','elem_score','walkscore']]
y = df['log_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.85, random_state=25)

print('X TRAIN: ', X_train, sep='\n')
print('')
print('X TRAIN VALUES: ', X_train.values.reshape(-1,1), sep='\n') #numpy.array - See above for how to supress scientific notation
'''
the reshape above will reshape into a single column.
'''