import pandas as pd
import numpy as np

dic1={
    'id': [1,2,3,4,5,6],
    'fname':['anu','jeni','kiran','rahul','jack','lilly'],
    'lname':['rose','k','j','das','joy','maria'],
    'age':[23,34,44,35,27,43]}
dic2={
    'prof':['python','python','bigdata','bigdata','java','java'],
    'salary':[2500,3400,2300,4500,3000,5000],
    'id':[4,5,6,7,8,9],
    'loc':['kannur','kozhikode','malappuram','kochi','alappuzha','kannur']
}

#df1 == is left
#df2 == is right


df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)
print(df1)
print("*"*100)
print(df2)
print("*"*100)

#we want fname,lname,age , prof,salary,loc
#newfname=pd.merge(df1,df2,on='columnname',how='type')

a=pd.merge(df1,df2,on='id',how='left') [['fname','lname','prof','salary','loc']]
print(a)