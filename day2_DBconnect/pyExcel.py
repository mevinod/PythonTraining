import pandas as pa


data = {'ID': [10, 11, 12], 'Name': ['A', 'B', 'C']}

df = pa.DataFrame(data)
print(df)

writer = pa.ExcelWriter('new.xlsx', index=False)
df.to_excel(writer, 'DataFrames')
writer.save()
print("Data is written to file - new.xlsx")


# Read Excel file

excel_file = 'new.xlsx'
data = pa.read_excel(excel_file, index=False)
df = pa.DataFrame(data)
print(df)
