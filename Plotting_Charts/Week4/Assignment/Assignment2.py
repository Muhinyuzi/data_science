%matplotlib notebook
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')

binsize=400
hashid='fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89'
df=pd.read_csv('data/C2A2_data/BinnedCsvs_d{}/{}.csv'.format(binsize,hashid))

df['Data_Value']=df['Data_Value'].apply(lambda x: x/10)

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Remove leap year
s_o=df.shape
df = df[~((df['Month']==2)&(df['Day']==29))]
s_r=df.shape
print('remove {} series ofdata'.format(s_o[0]-s_r[0]))

# Max and min data after grouping by each day:
max_0514 = df[(df['Element'] == 'TMAX') & (df['Year'] >= 2005)& (df['Year'] < 2015)].groupby(['Month','Day']).aggregate({'Data_Value':np.max})
min_0514 = df[(df['Element'] == 'TMIN') & (df['Year'] >= 2005)& (df['Year'] < 2015)].groupby(['Month','Day']).aggregate({'Data_Value':np.min})

max_2015 = df[(df['Element'] == 'TMAX') & (df['Year'] == 2015)].groupby(['Month','Day']).aggregate({'Data_Value':np.max})
min_2015 = df[(df['Element'] == 'TMIN') & (df['Year'] == 2015)].groupby(['Month','Day']).aggregate({'Data_Value':np.min})

broken_max = np.where(max_2015['Data_Value'] > max_0514['Data_Value'])[0]
broken_min = np.where(min_2015['Data_Value'] < min_0514['Data_Value'])[0]


plt.figure()

plt.plot(max_0514.values, label='Max  Temp (2005-2014)', linewidth=1,alpha = 0.7,c='salmon')
plt.plot(min_0514.values, label='Min   Temp (2005-2014)', linewidth=1,alpha = 0.7,c='royalblue')

plt.gca().fill_between(range(len(max_0514)), min_0514['Data_Value'],max_0514['Data_Value'], facecolor='azure', alpha=0.8)

# plt.xticks(range(0, len(max_0514), 20), max_0514.values[:,0].index[range(0, len(max_0514), 20)], rotation = '45')

plt.scatter(broken_max, max_2015.iloc[broken_max], s=10, color='red', label='High Temp Broken (2015)')
plt.scatter(broken_min, min_2015.iloc[broken_min], s=10, color='blueviolet', label='Low  Temp Broken (2015)')

plt.legend(loc = 'best', title='Temperature', fontsize=8)

plt.xticks(np.linspace(0,30 + 30*11 , num = 12), (r'Jan', r'Feb', r'Mar', r'Apr', r'May', r'Jun', r'Jul', r'Aug', r'Sep', r'Oct', r'Nov', r'Dec'), alpha = 0.8 )
plt.yticks(alpha = 0.8 )
plt.xlim(0,365)
plt.xlabel('Months', alpha = 0.8)
plt.ylabel('Temperature ($^\circ$C)', alpha = 0.8)
plt.title('Temperature Plot', alpha = 0.8)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_alpha(0.3)
plt.gca().spines['left'].set_alpha(0.3)

