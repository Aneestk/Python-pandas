import numpy as np
import pandas as pd

a=pd.read_csv("missing_data1.csv")
print(a.shape)

print("*"*100)
print(a.isna().sum())
print("*"*100)

#calories---> median
x=a['Calories'].median()
print(x)
print("*"*100)
a['Calories'].fillna(x,inplace=True)
print(a)