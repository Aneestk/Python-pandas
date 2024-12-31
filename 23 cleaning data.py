#pandas-cleaning data
#Data cleaning
#Data cleaning means fixing bad data in your data set.
#bad data could be:

#Emptycells
#Data in wrong format
#wrong data
#duplicates

import pandas as pd
df=pd.read_csv('data1.csv')
print(df.to_string())

#the data set contains some empty cells("Date" in row 22 and "calories" in row 18 and 28)

#the dat set contains wrong format("date" in row 26)

#the data set contain wrong format("duration" in row 7)

#the datan set contains duplicates (row 11 and 22)






