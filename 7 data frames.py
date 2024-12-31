#DataFrames

#Data sets in pandas are usually multy-dimensional tables,calld DataFrames

#series is like a column, a dataframe is a whole table
#create a dataframe from teo series
import pandas as pd

data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar=pd.DataFrame(data)
print(myvar)

#pandas DataFrame is a 2 dimensional data structure
#like a 2 dimensional array,or a table with rows and columns..