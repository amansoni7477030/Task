# Task

#Task 1
The code reads data from an Excel file named 'Task_Data.xlsx', converts the 'date' column to datetime format, groups the data by week using Monday as the start of the week, calculates the average of 'price1' for each week, and saves the result to a new CSV file named 'Task_1_average_price_per_week.csv'. The code assumes that the 'price1' column contains numerical data that can be averaged.

#Task 2
The code reads data from an Excel file named 'Task_Data.xlsx', creates a new column 'color' based on the condition 'price1 > price2', creates a new column 'min_price2' for each group of 3 consecutive 'R' rows containing the minimum value of 'price2' among them, selects the rows where the condition 'price1 > price2' is True and the middle row has the lowest value of 'price2' among all three of them, and saves the result to a new CSV file named 'Task_2_consecutive_R_with_min_price2.csv'.

#Task 3
The code reads data from an Excel file named 'Task_Data.xlsx', converts the 'date' column to a datetime object, filters the data for Mondays and Fridays using the 'day_name' attribute of the datetime object, and saves the result to a new CSV file named 'Task_3_mondays_fridays.csv'.
