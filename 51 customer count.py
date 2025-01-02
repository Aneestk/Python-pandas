import pandas as pd
import numpy as np

a=pd.read_csv("cust",header=None)
a.columns=['id','faname','lname','age','prof','location']

print(a.groupby('prof')['prof'].count().sort_values(ascending=False))
print("*"*100)

print(a.groupby('location')['location'].count().sort_values(ascending=False))
print("*"*100)
print(a.count())

print(a.loc[a['location']=='india'].groupby('prof')['prof'].count().sort_values(ascending=False))