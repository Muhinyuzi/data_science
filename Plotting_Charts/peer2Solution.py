import pandas as pd
import numpy as np
import calendar
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import matplotlib.pyplot as plt
data = pd.read_csv("data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv")
data['Date'] = pd.to_datetime(data['Date'])
data = data[~((data.Date.dt.month==2) & (data.Date.dt.day==29))]
data['year']=data.Date.dt.year
data['Month-Day'] = data.Date.dt.month.astype('str') + '-' + data.Date.dt.day.astype('str')

data_15= data[data['year']==2015].reset_index()
data_14= data[data['year']<2015].reset_index()

#data_max_15= data[data['Element']=='TMAX']
#data_min_15 = data[data['Element']=='TMIN']
#data_max_14= data[data['Element']=='TMAX']
#data_min_14 = data[data['Element']=='TMIN']

grouped_max_15= data_15[data_15['Element']=='TMAX'].groupby(['Month-Day']).agg({'Data_Value': max}).reset_index().rename(columns={'Data_Value':'Data_max'})
grouped_min_15= data_15[data_15['Element']=='TMIN'].groupby(['Month-Day']).agg({'Data_Value': min}).reset_index().rename(columns={'Data_Value':'Data_min'})
grouped_max_14= data_14[data_14['Element']=='TMAX'].groupby(['Month-Day']).agg({'Data_Value': max}).reset_index().rename(columns={'Data_Value':'Data_max'})
grouped_min_14= data_14[data_14['Element']=='TMIN'].groupby(['Month-Day']).agg({'Data_Value': min}).reset_index().rename(columns={'Data_Value':'Data_min'})

greater_than_14 = grouped_max_15[grouped_max_15>grouped_max_14]
lesser_than_14 = grouped_min_15[grouped_min_15< grouped_min_14]

ax = grouped_max_14.plot(label='Max Recorded', color='tab:red')
grouped_min_14.plot(ax=ax, label='Min Recorded', color='tab:blue')

plt.fill_between(grouped_max_14.index, grouped_max_14.Data_max, grouped_min_14.Data_min, alpha=0.10, color='tab:orange')

plt.scatter(greater_than_14.index,greater_than_14.Data_max, label = 'Max record of 2015', c = 'brown')
plt.scatter(lesser_than_14.index,lesser_than_14.Data_min,label = 'Min Record of 2015', c = 'green')
plt.legend()
#data_max
plt.xlim(0,360)
ticks = np.arange(0,370,30)
labels = list(calendar.month_abbr)
plt.xticks(ticks,labels)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.title('Daily Max/Min Temperatures for the year 2005-2014 ')

plt.ylabel('Temperature (C)', fontsize=10)
plt.xlabel('Day of the Year', fontsize=10)
ax.legend(loc=4,fontsize=6)



#plt.figure()
#plt.plot(grouped_max)