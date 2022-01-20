# pandas and numpy intro: how to create a dataframe, select and add columns, operations, and common methods

import pandas as pd
import numpy as np

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


from IPython.display import display

# creating an array
# data = np.array([[1,4],[2,5],[3,6]])
#
# creating a data frame
# df = pd.DataFrame(data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2'])
#
# print(df)
#
# create dataframe from dict
# states = ['ca', 'ga', 'wa', 'fl']
# populations = [10001038, 1904809, 102910491, 989718638]
#
# make the dict
# dict_states = {'States': states, 'Population': populations}
#
# create the dataframe
# df_pop = pd.DataFrame(dict_states)
#
# print(df_pop)

# create dataframe from csv file
print('\ndata from file:')
df_exams = pd.read_csv('StudentsPerformance.csv')
# print(df_exams)

# dataframe operations
# print(df_exams.head())
# print(df_exams.tail())
# print(df_exams.shape)
# display n rows
# pd.set_option('display.max_rows', 100)
# print(df_exams)
# print(df_exams.info())

# attributes
# print(df_exams.shape)
# print(df_exams.index)
# print(df_exams.columns)
# print(df_exams.dtypes)

# complex methods
# print(df_exams.describe())

# selecting a single column
# print(df_exams.gender)
# print(df_exams['math score'])

# selecting two or more columns
# print(df_exams[['gender', 'math score']])

# sorting values
# display(df_exams.sort_values('math score'))
# display(df_exams.sort_values('math score', ascending=False))

# average cols into new col
# df_exams['average'] = (df_exams['math score'] + df_exams['reading score'] + df_exams['writing score'])/3
# display(df_exams)

# value counts method
# print(df_exams['gender'].value_counts())
# print(df_exams['gender'].value_counts(normalize = True))
display(df_exams['parental level of education'].value_counts(normalize=True).round(3))
