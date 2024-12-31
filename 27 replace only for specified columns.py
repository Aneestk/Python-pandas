#Replace Only For Specified Columns

#The example above replaces all empty cells in the whole Data Frame.

#To only replace empty values for one column,
# specify the column name for the DataFrame:
#Replace NULL values in the "Calories" columns with the number 130: ?

import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)

print(df.to_string())

#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).