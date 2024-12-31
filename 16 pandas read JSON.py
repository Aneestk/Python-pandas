#pandas read JSON

#load the JSON file into a DataFrame

import pandas as pd

df=pd.read_json('jhai.json')

print(df.to_string())

#Tip: use to_string to print entire