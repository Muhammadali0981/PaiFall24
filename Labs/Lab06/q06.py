import pandas as pd 

df = pd.read_csv('alcohol-consumption-vs-gdp-per-capita.csv')
series = (df['Year'] == 1987) | (df['Year'] == 1989)
print(df[series])