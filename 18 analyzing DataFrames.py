#padas-analyzing DataFrames

#viewing the data
#the head() method returns the headers and specified rows
#starting from the top

#print the first 10 rows and headers of csv file as dataframe

import pandas as pd

df=pd.read_csv('data.csv')

print(df.head(10))