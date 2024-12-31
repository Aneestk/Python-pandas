#there is also a tail() method for viewing the last rows of the dataframe

#the tail() method return the headers and a specified number of rows
#the starting from the bottom

#print the last 5 rows of the dataframe

import pandas as pd

df=pd.read_csv('data.csv')

print(df.tail())