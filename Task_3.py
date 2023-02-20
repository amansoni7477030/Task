#Task 3
import pandas as pd

# read the CSV file into a pandas dataframe
df = pd.read_excel('Task_Data.xlsx')

# convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'])

# filter the data for Mondays and Fridays using the 'day_name' attribute
result = df[(df['date'].dt.day_name() == 'Monday') | (df['date'].dt.day_name() == 'Friday')]

# save the result to a new CSV file
result.to_csv('Task_3_mondays_fridays.csv', index=False)
