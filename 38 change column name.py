import pandas as pd
a=pd.read_csv("cust",header=None)
a.columns=['id','fname','lname','age','prof','location']
print(a)
print("*"*100)

#change column name prof to dpt
b=a.rename(columns={'prof':'dpt'})
print(b)