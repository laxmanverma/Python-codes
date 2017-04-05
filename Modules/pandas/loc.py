import pandas as pd

people=pd.read_csv('comma-separated_values.csv', index_col=0)
print(people.loc['SW'])
#print(people.loc['SW','JS'])#gives error?
print(people.loc[['SW','JS']])

"""With loc you can do practically any data selection operation on
DataFrames you can think of. loc is label-based, which means that
you have to specify rows and columns based on their row and column labels."""
#1
print('#1--------------------------------------')
print(people.loc['SW','Year'])         #it selects value of column year where
                                       #row value is equal to SW 
print(people.loc[['SW','JS'],["Name","Year"]])
