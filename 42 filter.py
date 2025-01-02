import numpy as np
import pandas as pd
a=pd.read_csv("cust",header=None)
a.columns=['id','fname','lnam','age','prof','location']

b=a.loc[a['age']==25]
print(b)
print("*"*100)


c=a.loc[a['location']=='india']
print(c)