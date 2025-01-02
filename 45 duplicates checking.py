#drop duplicates means drop the duplicates rows
import pandas as pd
a=pd.read_csv("cust",header=None)
a.columns=['id','fname','lname','age','prof','location']
print(a.duplicated().sum())
b=a.drop_duplicates()
print(b)

#drop duplicates row
