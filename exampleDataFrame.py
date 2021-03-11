import pandas as pd

df = pd.read_csv("Week2/datasets/presidents.csv", index_col=0)

print(df.head())
print(df['President'])

df['firstname'] = df['President'].apply(lambda x: x.split(' ')[0])
df['lastname'] = df['President'].apply(lambda x: x.split(' ')[-1])
#lastname = df['President'].split(' ')[-1]

#df['First'] = firstname
#df['Last'] = lastname


dfs = pd.read_csv("Week2/datasets/presidents.csv", index_col=0)
def row_creater(row):
	row['First'] = row['President'].split(' ')[0]
	row['Last'] = row['President'].split(' ')[-1]
	return row

dfs = dfs.apply(row_creater, axis='columns')	

print(dfs.head())

