import numpy as np
import pandas as pd
a=pd.read_csv("cust",header=None)
print(a)
print("*"*100)
a.columns=['id','fname','lname','age','prof','location']
print(a)
print("*"*100)
b=a[['fname','lname','age','prof']]
print(b)