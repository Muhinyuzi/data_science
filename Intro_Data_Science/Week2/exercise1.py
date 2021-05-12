import pandas as pd
import numpy as np

record1 = pd.Series({'Name':'Alice','Class':'Physics','Score':85})
record2 = pd.Series({'Name':'Jack','Class':'Chemistry','Score':82})
record3 = pd.Series({'Name':'Helen','Class':'Biology','Score':90})

df = pd.DataFrame([record1,record2,record3], index=['school1','school2','school1'])

print(df)
print(df.head(1))

students = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]

df = pd.DataFrame(students, index=['school1','school2','school1'])  

print(df)     

print(df.loc["school2"])     

print(df.loc["school1","Name"]) 
print(df.T)
print(df.T.loc['Name'])
print(df.loc[:,['Name','Score']])
#drop doesnt remove the school1 but it makes a copy of df with school1 removed.
print(df.drop(["school1"]))
print(df) 

#make a copy of a DataFrame using copy()
copy_df = df.copy()
#Drop the Name column is this copy
#axis = 1 because it a Column
copy_df.drop("Name",inplace=True,axis=1)
print(copy_df)

del copy_df['Class']
print(copy_df)

copy_df['Class_ranking'] = None
print(copy_df)
