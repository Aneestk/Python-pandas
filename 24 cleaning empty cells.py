#pandas-- cleaning empty cells

#return a new data frame with no empty cells

import pandas as pd

df=pd.read_csv('data1.csv')
print(df)
new_df =df.dropna()

print(new_df.to_string())

#Note: by defualt ,the dropna() method returns a new data frame
#and will not change the original
#non values row will be deleted

