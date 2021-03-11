import pandas as pd
import numpy as np


records1 = pd.Series({'Name':'Claude', 'Class':'Biology','Age':35})
records2 = pd.Series({'Name':'Richard', 'Class':'Computer','Age':33})
records3 = pd.Series({'Name':'Runa', 'Class':'Economy','Age':34})

df = pd.DataFrame([records1,records2,records3],index=["school1","school2","school1"])

print(df)

students = [{'Name':'Claude', 'Class':'Biology','Age':35},{'Name':'Richard', 'Class':'Computer','Age':33},
            {'Name':'Runa', 'Class':'Economy','Age':34}]

df1 = pd.DataFrame(students,index=["school1","school2","school1"])  
print(df1)
print(df1.T)
print(df.index) 
df['Sex'] = None
print(df) 
print(df1.loc["school1","Name"])
print(df1.loc["school2","Name"])     

copy_df = df1.copy()
copy_df.drop("school2",inplace=True,axis=0)
print(copy_df)

df = pd.read_csv('Week2/datasets/Admission_Predict.csv', index_col=0)
df.columns = (x.lower().strip() for x in df.columns)

print(df.columns)


