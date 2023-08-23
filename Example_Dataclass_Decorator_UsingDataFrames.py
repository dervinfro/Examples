from dataclasses import dataclass, field
import pandas as pd
'''
What I wanted to test here was the ability to pass in a DataFrame as a variable to a class.  I was not sure what that looked like, but it appears it is as easy as:
data: pd.DataFrame

Very easy stuff...by doing this I am able to test repr(external_dataframe) and str(external_dataframe).
'''
@dataclass
class Fruit:
    data: pd.DataFrame  # <- This was my guy I was looking into.

    @classmethod
    def calculate_total_price(cls, dataframe, price):
        dataframe['total_price'] = dataframe['weight (kg)'] * price
        return dataframe

# Create an external DataFrame
data = {
    'fruit': ['Apple', 'Banana', 'Apple', 'Banana'],
    'supplier': ['T & C Bro', 'T & C Bro', 'JM Wholesales', 'JM Wholesales'],
    'weight (kg)': [1000, 2000, 3000, 4000],
    'customer_rating': [4.8, 3.2, 4.2, 4.3]
}
external_dataframe = pd.DataFrame(data)

# Calculate total price for the external DataFrame
price = 2.5  # Example price
updated_dataframe = Fruit.calculate_total_price(external_dataframe.copy(), price)
print(updated_dataframe)
