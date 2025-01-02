import pandas as pd
a=pd.read_csv("Temperature",header=None,sep= " ")
a.columns=['year','temp']


#syntax
#newdfname=olddfname.groupby('columnname')["columnname'.sum()
b=a.groupby('year')['temp'].sum().sort_values(ascending=False)
print(b)