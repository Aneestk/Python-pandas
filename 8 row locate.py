#Locate row

#pandas use the loc attribute to return one or more specified row

#return row 0
import pandas as pd

data={
    "calories":[420,380,390],
    "duration":[50,40,45]
}

#load data into a DataFrame object
myvar=pd.DataFrame(data)
print(myvar)
print(myvar.loc[0])

