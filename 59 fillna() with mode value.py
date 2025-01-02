import numpy as np
import pandas as pd
a=pd.read_csv("missing_data1.csv")
print(a.shape)
print("*"*100)
print(a.info())
print("*"*100)
print(a.isna().sum())
print("*"*100)

#date---> mode
x=a['Date'].mode()[0]
print(x)
print("*"*100)
a['Date'].fillna(x,inplace=True)
print(a)

print("*"*100)
print(a.isna().sum())
