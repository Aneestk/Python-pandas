#for droping column drop() is used

import pandas as pd
a=pd.read_csv("cust",header=None)
a.columns=['id','fname','lname','age','prof','location']
b=a.drop(['prof','location'],axis=1)
print(b)