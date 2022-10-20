# Pandas
import pandas as pd

sales1 = pd.read_csv('sales1.csv', index_col=None, encoding='utf-8')
sales2 = pd.read_csv('sales2.csv', index_col=None, encoding='utf-8')

print(sales1)
print(len(sales1)) # number of rows
print(sales1.head(1)) # subset of data frame, from top
print(sales1.tail(1)) # subset of data frame, from bottom

# filter
print(sales1['Book title'] + ' hello') # extract into a series object, and can do math like a numpy object
# or pick sales1.col_name -> make sure there are no spaces
print(sales1['Number sold'] > 10) # extract into a series object, and can do math like a numpy object

# comparision returns an array of true and false, that can be used to filter
print(sales1[sales1['Number sold'] > 10].sort_values('Number sold'))
print(sales1[(sales1['Number sold'].notnull()) & (sales1['Number sold'] < 30)])  # can't use logical and since the boolean value of a series in undefined

print([0]) # [0]
print([0]*10) # [0, 0, ...] not [[0], [0], ....]
print([[0]*10]*10) # [[0, 0, ...], [0, 0, ...]...]
rows, cols = (10, 10)
arr = [[0]*cols]*rows

# Python uses shallow lists. Only one integer object gets created
rows, cols = (10, 10)
arr = [[0 for i in range(cols)] for j in range(rows)]
