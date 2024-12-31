#create  csv file

import pandas as pd
import numpy as np
data={'Duration':[60,60,60,60],
      'Data':[np.nan,np.nan,'2020/11/09','2020/12/10'],


      'Pulse': [110,110,117,103,],
      'Maxpulse':[130,130,145,13510,],
      'Calories':[409.1,409.1,np.nan,230.0,]


      }
df=pd.DataFrame(data)
print(df)
df.to_csv('create.csv')