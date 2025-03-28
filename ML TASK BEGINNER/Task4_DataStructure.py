import pandas as pd
csvframe = pd.read_csv('people_data.csv')
print(csvframe)                                             #Original Dataset
csvframe.index = ['one', 'two', 'three', 'four', 'five']    #Reindexing
print(csvframe)
print(csvframe.sort_index(axis=1))                          #Sorts by column name as axis=1 signifies columns
print(csvframe.sort_index())                                #Sorts by index name 
print(csvframe[csvframe['Sex'] == 'Male'])                  #Filters the data to give the details of perople who are male


