import pandas as ps


data = {'ID': [10, 11, 12], 'Name': ['A', 'B', 'C']}

df = ps.DataFrame(data)
try:
    df.to_csv('test.csv', index=False)
    print('Data written successfully')
    print(df.head(1))
    df.sort_values(by=['B'])
    print(df.tail(1))
except Exception as e:
    print('Some error writing to the file', e)

"""
print(df.columns)
print('df,set_index[['SID','Name']])
print(df.[1:3])

newdf = df.fillna{{
'Name' : 'Not updated',
'Design' : 'Not given',
'Loca' : 'confirmed'
}}
print (newdf)
"""