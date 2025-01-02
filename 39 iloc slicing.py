import numpy as np
import pandas as pd
a=pd.read_csv("Temperature",header=None,sep=" ")
print(a)
print("*"*100)
print(a.iloc[5:12])
print("*"*100)
print(a.iloc[1])
print("*"*100)
print(a.iloc[:10])
print("*"*100)
print(a.iloc[10:])