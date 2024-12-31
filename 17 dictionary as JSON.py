#dictionary as JSON

#JSON=pythin dictionary

#JSON objects have the same format as python dictionaries

#load a python dictionary into a dataframe

import pandas as pd
data={
    "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
    },
    "Pulse":{
        "0":192,
        "1":110,
        "2":117,
        "3":103,
        "4":109,
        "5":117
    },
    "Maxpulse":{
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories":{
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}
df=pd.DataFrame(data)
print(df)