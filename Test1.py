import pandas as pd
df= pd.read_excel('E:/Study\python/24-july/data fsds_/Attribute DataSet.xlsx')
print(df)
Sudh=df.tail(1)
print(Sudh)

df3 = pd.read_csv('E:/Study\python/24-july/data fsds_/haberman.csv', header= None , names= ['age','yearofoperation','days taken inoperation', 'survival status'])
print(df3)

df4 = pd.read_csv("raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/FIFA_country_codes.csv")
print(df4)

print(df)