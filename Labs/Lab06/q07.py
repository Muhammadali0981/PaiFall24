import pandas as pd 

df = pd.read_excel('employee.xlsx')
bool_series = (df['Year'] == 2016) 
print(df[bool_series])