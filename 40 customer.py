import pandas as pd
a=pd.read_csv("cust",header=None)
print(a.head())
x=a.iloc[:,:-1]   #all rows ,all columns exept last columns
y=a.iloc[:,-1]
print(x)
print("*"*100)
print(y)