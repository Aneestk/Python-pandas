import pandas as pd
a=pd.read_csv("sample4.txt",header=None)
a.columns=['id','fname','lname','age','phone_no','loc']
print(a)

#there are 5 evaluating functions
#1.count   3.min
#2.max       4.sum     5.avarage


#count-oro columnthinm corresponding count kand pidikka

b=a.groupby('loc')['loc'].count()
print(b)