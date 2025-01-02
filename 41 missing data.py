import pandas as pd
a=pd.read_csv("missing_data1.csv")
print(a.isna().sum())  #null value
print("*"*100)
b=a.fillna('150')
print('b')
print("*"*100)
print(b.isna().sum())