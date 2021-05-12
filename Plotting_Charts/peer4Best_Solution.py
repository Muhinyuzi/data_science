import matplotlib.pyplot as plt
import mplleaflet
import numpy as np
import pandas as pd

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

df['Date'] = pd.to_datetime(df.Date)

df = df.sort('Date')

#new_df = df[df['Date'] == '2005-01-02']
#new_df['Data_Value'].min()


df2015 = df[df['Date'].dt.year == 2015]

df = df[df['Date'].dt.year != 2015]

df.head()

max_temps = list()
min_temps = list()
dates = list()


df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year





for group, frame in df.groupby(['Month', 'Date']):  
    max_temps.append(frame['Data_Value'].max())
    min_temps.append(frame['Data_Value'].min())
    dates.append(group[1])

dates    

new_df = df.copy() 

new_df['Day'] = new_df['Date'].dt.day


new_df

new_max = list()
new_min = list()
days = list()
for group, frame in new_df.groupby(['Month', 'Day']):
    new_max.append(max(frame['Data_Value']))
    new_min.append(min(frame['Data_Value']))
    days.append(group)
len(new_max)

max_list = [e/10 for e in new_max]

min_list = [e/10 for e in new_min]
min_list
plt.plot(max_list, color = 'r')
plt.plot(min_list, color = 'b')
plt.gca().fill_between(range(len(max_list)), max_list, min_list, facecolor='orange', alpha=0.35)
plt.xlim([0, 366])
plt.xlabel('Days', fontsize=16)
plt.ylabel('Temperature in degrees C', fontsize=16)
plt.title("Ann Arbor's Record High and Low Temperatures for 2005-2014", fontsize=18)
plt.rcParams['figure.figsize'] = [15, 12]
plt.show()
df2015['Month'] = df2015['Date'].dt.month
df2015['Day'] = df2015['Date'].dt.day

df2015['New_Values'] = df2015['Data_Value'].apply(lambda x: x/10)
max15 = list()
min15 = list()

for group, frame in df2015.groupby(['Month', 'Day']):
    max15.append(max(frame['New_Values']))
    min15.append(min(frame['New_Values']))
    
len(min15)
len(max15)

df1 = pd.DataFrame(columns = ['DATE','MAX 05-14', 'MIN 05-14'])
df1['MAX 05-14'] = max_list
df1['MIN 05-14'] = min_list
df1['DATE'] = days


df1 = df1.drop([59])

df1.reset_index(inplace=True)
df1 = df1.drop(['index'], axis= 1)
df1

df1['MAX 15'] = max15
df1['MIN 15'] = min15

df2 = df1[df1['MAX 15'] > df1['MAX 05-14']]
df3 = df1[df1['MIN 15'] < df1['MIN 05-14']]

df3

plt.plot(df1.index, df1['MAX 05-14'], color = 'red', alpha=0.5, label='Record Highs 2005-14 ')
plt.plot(df1.index, df1['MIN 05-14'], color = 'blue', alpha=0.5, label ='Record Lows 2005-14')
plt.scatter(df3.index, df3['MIN 15'], s=40, c='b', label ='Record Lows 2015')
plt.scatter(df2.index, df2['MAX 15'], s=40, c='r', label ='Record Highs 2015')
plt.gca().fill_between(range(len(max_list)), max_list, min_list, facecolor='purple', alpha=0.1)
plt.xlim([-1, 366])
plt.xlabel('Days', fontsize=16)
plt.ylabel('Temperature in degrees C', fontsize=16)
plt.title("Ann Arbor's Record High and Low Temperatures for 2005-2014", fontsize=18)
plt.legend(title='Legend')
plt.show()