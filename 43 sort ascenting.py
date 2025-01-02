import pandas as pd
a=pd.read_csv("cust",header=None)
a.columns=['id','fname','lname','age','prof','location']
b=a.sort_values(by='age',ascending=False)
print(b)
