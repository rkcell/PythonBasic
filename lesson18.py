import pandas as pd
print(pd.__version__)
#df= pd.read_csv("foods.csv", usecols=["First Name", "Gender", "City"], index_col="First Name")
df= pd.read_csv("foods.csv")
print(df.info())
print(df.describe())
print(df.columns)

array=pd.Series([1, 2, 3]).values
print(array)

#Claude
#Seaborn