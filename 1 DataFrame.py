import pandas as pd

mydataset={
    'cars':["BMW","Ford","Volvo"],
    'passings':[3,7,2]
}
myvar=pd.DataFrame(mydataset)
print(myvar)