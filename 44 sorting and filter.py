import pandas as pd
a=pd.read_csv("sample4.txt",header=None)
a.columns=['id','fname','lname','age','phone_no','loc']
print(a.loc[a['age']>23] [['fname','lname','age']])


print(a)
print("*"*100)
print(a.sort_values(by='age',ascending=False) [['fname','lname','age','phone_no']].head(2))
print("*"*100)

print(a.sort_values(by='age')[['fname','lname','phone_no','loc','age']].head(1))
print(a.loc[a['loc']=='chennai'].sort_values(by='age',ascending=False)
      [['fname','lname','age','phone_no','loc']].head(3))