import pandas as pd
df=pd.read_csv(r"C:\Users\Supriya\Downloads\death-rate-from-suicides-gho new.csv")
print(df)
print(df.isna().sum())
print(df.shape)  # rows and columns in data
print(df.info())  # columns, non-null values count.datatype of each column,memory usage
# Indexing and Selecting Data
# 
print(df.)