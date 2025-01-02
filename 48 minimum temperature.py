import pandas as pd
a=pd.read_csv("Temperature",header=None,sep= " ")
a.columns=['year','temp']


#syntax
#newdfname=olddfname.groupby('columnname')["columnname'.min()
b=a.groupby('year')['temp'].min().sort_values(ascending=False)
print(b)