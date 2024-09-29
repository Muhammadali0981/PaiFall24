import pandas as pd 

dp = pd.read_csv('products.csv')
do = pd.read_csv('orders.csv')

joined_df = pd.merge(dp, do, how='inner', on='ProductID')
joined_df["Revenue"] = joined_df["Price"] * joined_df["Quantity"]
joined_df['Order Date'] = pd.to_datetime(joined_df['Order Date'], format='%m-%d-%Y')
highest_revenue_row = joined_df.loc[joined_df['Revenue'].idxmax()]


joined_df['Year'] = joined_df['Order Date'].dt.year
joined_df['Month'] = joined_df['Order Date'].dt.month

monthly_revenue = joined_df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()

monthly_revenue.columns = ['Year', 'Month', 'Total Revenue']

joined_df = joined_df.dropna(subset=['ProductID', 'ProductName', 'Order ID', 'Quantity'])
joined_df['Price'] = pd.to_numeric(joined_df['Price'], errors='coerce')
joined_df = joined_df.dropna(subset=['Price'])


print("First 5 Products: \n", dp.head(5))
print("First 5 Orders: \n", do.head(5))
print("Last 10 Products: \n", dp.tail(10))
print("Last 10 Orders: \n", do.tail(10))
print("Total Revenue From Orders: \n", joined_df["Revenue"].sum())
print("Top 5 Best Selling Products: \n", joined_df["Revenue"].nlargest(5))
print("Top 5 Low Selling Products: \n", joined_df["Revenue"].nsmallest(5))
print("Top 5 Best Selling Products Common: \n", joined_df["Revenue"].nlargest(5).mode())
print("Average of Products of Each Category: \n", dp.groupby('Category')['Price'].mean())
print("Day of Highest Revenue: ", highest_revenue_row["Order Date"].day, "Month: ", highest_revenue_row["Order Date"].month, "Year: ", highest_revenue_row["Order Date"].year)
print(monthly_revenue)