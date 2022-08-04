import pandas as pd


df= pd.read_excel('E:/Study\python/24-july/data fsds_/Attribute DataSet.xlsx')

Json = df.to_json('test1234.json')
df.to_json('E:/Study/python/24-july/test123.json')

df5 = pd.read_json('E:/Study/python/24-july/test123.json')
print(df5)

