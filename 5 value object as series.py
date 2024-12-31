#key/value object as series

#you can also use key/value object
#like a dictionary when creating an object

#create a simple pandas series from a dictionary

import pandas as pd

calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)