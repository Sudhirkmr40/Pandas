import pandas as pd
import  openpyxl

df= pd.read_excel('E:/Study\python/24-july/data fsds_/Attribute DataSet.xlsx')
print(df)
type(df)

df2= pd.read_excel('E:/Study\python/24-july/data fsds_/Attribute DataSet.xlsx' , sheet_name = 'Sheet2', header=None , names= ['A','B'])
print(df2)
type(df2)
#
df.head(2)





