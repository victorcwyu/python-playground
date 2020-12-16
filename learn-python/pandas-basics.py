import pandas as pd

# key data structure is the DataFrame
# DataFrames allow the storage/manipulation of tabular data
# in rows of observations and columns of variables

# one way to create a DataFrame is using a dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

brics = pd.DataFrame(dict)
# print(brics)

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
# print(brics)

# DataFrames can also be created by importing a csv file using Pandas
cars = pd.read_csv('cars.csv')
# print(cars)

# indexing DataFrames
# index_col can be set
cars = pd.read_csv('cars.csv', index_col=0)
# print(cars)

# single bracket = Pandas Series
# print(cars['cars_per_cap'])

# double bracket = Pandas DataFrame
# print(cars[['cars_per_cap']])

# print out DataFrame with country and drives_right columns
# print(cars[['cars_per_cap', 'country']])

# square brackets can also be used to access observations (rows) from a DataFrame

# print out first 4 observations
# print(cars[0:4])

# print out fifth and sixth observation
# print(cars[4:6])

# loc and iloc perform just about any data selection operation
# loc is labels-based
# iloc is integer index based

# print out observation for Japan
print(cars.loc[['AUS', 'EG']])

# print out observations for Australia and Egypt
print(cars.iloc[2])
