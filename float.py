import  pandas as pd

data = pd.read_csv('E:/Study/python/30 july/sales_data_final.csv')
print(data)

x= data.columns
print(x)

y =data[data.dtypes[data.dtypes == float].index]
print(y)

z = data.order_id
print(z)
print(data)

t = data['category1'] = 'shakya'
print(t)

z = data.columns
print(z)

j = data['order_id'].isnull()
print(j)

k = data.dtypes['order_id']
print(k)