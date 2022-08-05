import  pandas as pd

data = pd.read_csv('E:/Study/python/30 july/sales_data_final.csv')
print(data)
#
data.head()
data.tail()
s = data.columns
print(s)

x= data['order_date']
print(x)
type(x)
y =data.dtypes
print(y)
z=data[['profit','year','sales']]
print(z)

t = data[['country', 'market', 'region']]
print(t)

z = data.describe()
print(z)
y =data[data.dtypes[data.dtypes == 'object'].index].describe()
print(y)

