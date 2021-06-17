import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
This is an example problem for housing data using scatterplots and normalized house data.
'''

df = pd.read_csv('/Users/user/Downloads/ML Analytics/ML Analytics - Course 1/assignment2.csv')
columns = ['Longitude', 'Latitude', 'Sale_Price']

print(df.head())

df_sale_filtered_low = df[df['Sale_Price'] < 10].index 
'''
NOTE: The output of .index (SEE ABOVE) returns the index of each of the rows
ie: Int64Index([   9,   19,   33,   52,   53,   56,   60,   83,   88,  108,
		...
		9829, 9859, 9866, 9877, 9878, 9897, 9927, 9954, 9968, 9989]
		
It DOES NOT return the full row/column outputs.  
To get the full return of row/column outputs, remove the .index
'''
df = df.drop(df_sale_filtered_low)


def normalize(value):
	norm = value / 100000
	return norm
	
col = 'Sale_Price'
df[col] = df[col].apply(normalize)

df_sale_filtered_high = df[df['Sale_Price'] > 7].index
df = df.drop(df_sale_filtered_high)

print(df[col].describe())

print(df.shape)



df.plot(kind='scatter', x='Longitude', y='Latitude', alpha=0.4, 
		label='population', figsize=(10,7), c='Sale_Price', cmap=plt.get_cmap('jet'), colorbar=True)
plt.show()