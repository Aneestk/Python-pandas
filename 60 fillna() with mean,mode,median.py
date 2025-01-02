import numpy as np
import pandas as pd
a=pd.read_csv("travel-times.csv")
print(a.isna().sum())

##date---> mode
##distance---> mean
##AvgMovingSpeed---> median
##FuelEconomy---> mode

#date---> mode
x=a['Date'].mode()[0]
print(x)
print("*"*100)
a['Date'].fillna(x,inplace=True)
print(a)
print("*"*100)

#distance---> mean
x=a['Distance'].mean()
print(x)
print("*"*100)
a['Distance'].fillna(x,inplace=True)
print(a)
print("*"*100)


#AvgMovingSpeed---> median
x=a['AvgMovingSpeed'].median()
print(x)
print("*"*100)
a['AvgMovingSpeed'].fillna(x,inplace=True)
print(a)
print("*"*100)

#FuelEconomy---> mode
x=a['FuelEconomy'].mode()[0]
print(x)
print("*"*100)
a['FuelEconomy'].fillna(x,inplace=True)
print(a)

print("*"*100)

print(a.isna().sum())
