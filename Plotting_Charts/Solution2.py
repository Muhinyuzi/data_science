import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np
%matplotlib notebook

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df['Data_Value']=df['Data_Value'].apply(lambda x: x/10)
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
cond1 = df['Month']==2
cond2 = df['Day']==29
df = df[~(cond1 & cond2)]
df_2015 = df[df['Date'] > '2014']
condition1 = df['Date'] >= '2005' 
condition2 = df['Date'] <= '2014'
df = df[condition1 & condition2]

high = df[df['Element']  == 'TMAX']
high = high.groupby(['Month','Day']).agg({"Data_Value":np.max})
high_2015 = df_2015[df_2015['Element']  == 'TMAX']
high_2015 = high_2015.groupby(['Month','Day']).agg({"Data_Value":np.max})
high_record_broken_2015 = np.where(high_2015['Data_Value'] > high['Data_Value'])


low = df[df['Element']  == 'TMIN']
low = low.groupby(['Month','Day']).agg({"Data_Value":np.min})
low_2015 = df_2015[df_2015['Element']  == 'TMIN']
low_2015 = low_2015.groupby(['Month','Day']).agg({"Data_Value":np.min})
low_record_broken_2015 =np.where(low_2015['Data_Value'] < low['Data_Value'])
#print(low_2015.head())
#print(low_record_broken_2015)
#print(high_2015.iloc[high_record_broken_2015])



plt.figure(figsize=(8,7))

#plt.plot(high.values, '-',low.values, '-',linewidth=1,alpha = 0.7)
plt.plot(high.values, label='Temp_Max_2005-2014', linewidth=1,alpha = 0.7,color='orange')
plt.plot(low.values, label='Temp_Min_2005-2014', linewidth=1,alpha = 0.7,color='blue')
plt.xticks(np.arange(0,365 , step=31), 
           ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'), alpha = 0.9 
          ,rotation=30)

plt.gca().fill_between(range(len(high)), low['Data_Value'],high['Data_Value'], facecolor='grey', alpha=0.1)
plt.scatter(high_record_broken_2015, high_2015.iloc[high_record_broken_2015],s=8, color='red', label='Broken_record_High_Temp_2015')
plt.scatter(low_record_broken_2015, low_2015.iloc[low_record_broken_2015],s=8, color='green', label='Broken_record_Low_Temp_2015')
plt.xlabel('Months')
# add a label to the y axis
plt.ylabel('Temperatures (In Celsius Degrees)')
# add a title
plt.title(' Global Historical Temperatures(2005-2015)')
plt.xlim(0,365)
plt.legend()
plt.legend(loc=4, frameon=False, title='Temperatures')

plt.tick_params(top='off', bottom='on', left='on', right='off', labelleft='on', labelbottom='on',colors='r')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.savefig('Temperatures.png')




def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

#leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')