import pandas as pd 

df = pd.read_excel('employee.xlsx')
bool_series = (df['Year'] == 2020) 
print(df[bool_series])