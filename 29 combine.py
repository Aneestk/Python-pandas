import pandas as pd
a=pd.Series([1,2,4,5])
b=pd.Series([6,7,9,2])
c=a.append(b,ignore_index=True)
print(c)