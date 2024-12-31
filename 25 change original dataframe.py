#if you want to change the original dataframe
#use the inplace =True argument


#remove all rows with null values

import pandas as pd
df = pd.read_csv('data1.csv')
df.dropna(inplace = True,ignore_index=True)
print(df.to_string())

#Note: now the dropna(inplace =True)
#will not return a new data frame
#but it will remove all rows containing null values
#from the original dataframe