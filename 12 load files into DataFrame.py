#load files into DataFrame

#if your data sets are stored in a file,pandas can load them into a DataFrame

#load a Comma Separated File(CSV file) into DataFrames
import pandas as pd
df=pd.read_csv('data.csv')
print(df)