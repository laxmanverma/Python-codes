import pandas as pd

#1
print('#1-------------------------------')
dataframe = pd.read_csv('comma-separated_values.csv')
print(dataframe)
"""The DataFrame is one of Pandas' most important data structures.
It's basically a way to store tabular data, where you can label the
rows and the columns."""

#2
print('#2-------------------------------')
dataframe = pd.read_csv('comma-separated_values.csv', index_col=0)
"""index_col, is an argument of read_csv() that you can use to specify
which column in the CSV file should be used as a row label.
Hera it is set as 0 so that the first column is used as row label."""
print(dataframe)

#3
print('#3--------------------------------')
dataframe = pd.read_csv('comma-separated_values.csv', index_col=1)
print(dataframe)

#4
print('#4--------------------------------')
dataframe = pd.read_csv('comma-separated_values.csv')
print(dataframe['Place'])#Print out Place column as Pandas Series
print(dataframe[['Place']])# Print out Place column as Pandas DataFrame
