import pandas as pd
data=[[100,'ali','khan',23,'python','kannur',2000],
      [101,'rahul','h',25,'python','kozhikode',3000],
      [102,'anees','j',34,'python','vazhakkad',2400]]
a=pd.DataFrame(data,columns=['id','fname','lname','age','prof','place','salary'])
a['dpt']=['AHN','SHG','DFG','RTY','TOE']
print(a)