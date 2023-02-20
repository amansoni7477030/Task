#Task 2
import pandas as pd

# read the CSV file into a pandas dataframe
df = pd.read_excel('Task_Data.xlsx')

# create a new column 'color' based on the condition price1 > price2
df['color'] = df.apply(lambda row: 'R' if row['price1'] > row['price2'] else 'G', axis=1)

# create a new column 'min_price2' for each group of 3 consecutive 'R' rows, containing the minimum value of price2 among them
df['min_price2'] = df.groupby((df['color'] != df['color'].shift()).cumsum(), group_keys=False)['price2'].apply(lambda x: x.rolling(window=3, min_periods=1).min().shift(-1))

# select the rows where the condition price1 > price2 is True and the middle row has the lowest value of price2 among all three of them
result = df[(df['color'] == 'R') & (df['price2'] == df['min_price2'])]
#Save in csv file
result.to_csv('Task_2_consecutive_R_with_min_price2.csv', index=False)
