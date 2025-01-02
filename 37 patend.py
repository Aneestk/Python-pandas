import pandas as pd
a=pd.read_csv("patent",header=None,sep=" ")
print(a)
print("*"*100)
a.columns=['patent','sub_patent']
print(a)