#max_raows
#the number of rows returned is defined in pandas option settings

#you can check your system's maximum rows
#with the pd.options.display.max_rows statement.

#check the number of maximum returned rows

import pandas as pd

print(pd.options.display.max_rows)

#in my system the number is 60
#which means thst the datat form contains more than 60 rows
#the print(df) statement will return only the headers and the first and last 5 rows