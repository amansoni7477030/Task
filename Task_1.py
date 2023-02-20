 #Task 1
import pandas as pd

# Read the data from 'task.xlsx' file
df = pd.read_excel('Task_Data.xlsx')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Group the data by week and calculate the average of price1 for each week
df_weekly = df.groupby(pd.Grouper(key='date', freq='W-MON')).mean()

# Reset the index and rename the columns
df_weekly = df_weekly.reset_index().rename(columns={'price1': 'average price'})

# Save the data to a new csv file
df_weekly.to_csv('Task_1_average_price_per_week.csv', index=False)
