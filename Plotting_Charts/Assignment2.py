
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as dates
import matplotlib.ticker as ticker

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df['Data_Value'] = df['Data_Value']*0.1
df['Year'] = pd.DatetimeIndex(df['Date']).year.astype(int)
df['Date'] = pd.to_datetime(df['Date'])
df['MD'] = df['Date'].dt.strftime('%m-%d')
df = df[df['MD']!='02-29']


date = np.arange('2015-01-01','2016-01-01', dtype='datetime64[D]')


tmax = pd.DataFrame(df[(df['Element']=="TMAX") & (df["Year"] > 2004) & (df["Year"] < 2015)].groupby(['MD','Element'])['Data_Value'].max()).reset_index()
tmin = pd.DataFrame(df[(df['Element']=="TMIN") & (df["Year"] > 2004) & (df["Year"] < 2015)].groupby(['MD','Element'])['Data_Value'].min()).reset_index()

newdf = tmax.append(tmin).sort_values(by="MD")
maxvalue = newdf[newdf['Element'] == "TMAX"]['Data_Value']
minvalue = newdf[newdf['Element'] == "TMIN"]['Data_Value']

max2015 = df[(df.Year==2015) & (df['Element']=="TMAX")].groupby(['MD','Element'])['Date', 'Data_Value'].max().reset_index().sort_values(by="MD")
max2015 = max2015.merge(tmax, on="MD")


min2015 = df[(df.Year==2015) & (df['Element']=="TMIN")].groupby(['MD','Element'])['Date', 'Data_Value'].min().reset_index().sort_values(by="MD")
min2015 = min2015.merge(tmin, on="MD")
plt.plot(date,maxvalue, color="red", alpha=0.5,linewidth=0.8)
plt.plot(date,minvalue, color="skyblue", linewidth=0.8)
plt.title('2005-2015 Temperatures in\nAnn Arbor, Michigan, United States')
plt.xlabel('Date')
plt.ylabel('Temp (Celsius)')



recordhigh = max2015[(max2015.Data_Value_x > max2015.Data_Value_y)]
plt.scatter(recordhigh.Date.values, recordhigh.Data_Value_x.values, color='red', s=8)

recordlow = min2015[(min2015.Data_Value_x < min2015.Data_Value_y)]
plt.scatter(recordlow.Date.values, recordlow.Data_Value_x.values, color='blue', s=8)


plt.legend(['Record high (2005-2014)','Record low (2005-2014)','Record breaking high in 2015','Record breaking low in 2015'],loc=0,frameon=False,)

ax = plt.gca()
ax.fill_between(date_index, maxvalue, minvalue, facecolor='grey', alpha=0.15)

ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
ax.axis(['2015/01/01','2015/12/31',-50,50])
plt.show()

