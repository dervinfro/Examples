# https://towardsdatascience.com/settingwithcopywarning-in-pandas-782e4aa54ff7

import pandas as pd

# Create an external DataFrame
data = {
    'fruit': ['Apple', 'Banana', 'Apple', 'Banana'],
    'supplier': ['T & C Bro', 'T & C Bro', 'JM Wholesales', 'AN Fittings'],
    'weight (kg)': [1000, 2000, 3000, 4000],
    'customer_rating': [4.8, 3.2, 4.2, 4.3]
}
external_dataframe = pd.DataFrame(data)

'''
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  external_dataframe[external_dataframe.supplier  == 'AN Fittings']['customer_rating'] = 4.9
'''
# This line filters down to the Supplier of AN Fittings
external_dataframe[external_dataframe.supplier  == 'AN Fittings']

# Here is how the SettingWithCopyWarning gets generated
# Notice the two sets of brackets
external_dataframe[external_dataframe.supplier  == 'AN Fittings']['customer_rating'] = 4.1

# This did not generate the above error due to: .loc and everything is single brackets.
# Notice this from line 15 Above: Try using .loc[row_indexer,col_indexer] = value instead
# row_indexer is equal to external_dataframe.supplier  == 'AN Fittings
# col_indexer is equal to 'customer_rating'] = 4.9
external_dataframe.loc[external_dataframe.supplier  == 'AN Fittings','customer_rating'] = 4.9

# There are some functions like the groupby function, which does not return a view or copy but only the grouped object

