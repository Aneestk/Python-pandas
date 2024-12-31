#pandas read CSV

#if you have large DataFrame wit many rows

#to__string() used to print entire DataFrame
import pandas as pd

df=pd.read_csv('big.csv')
print(df.to_string())

#print(df) method
#will only return first five rows and last five rows