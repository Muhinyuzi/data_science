#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[19]:


import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]
    
    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[3]:


get_ipython().magic('matplotlib notebook')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[106]:


df = pd.read_csv('data/C2A2_data/BinnedCsvs_d25/391a2922ad597ba080f4b99dea6d62842562d64845ef5df1a384561e.csv', parse_dates=["Date"])
df['year'] = pd.DatetimeIndex(df['Date']).year
df=df[~((pd.DatetimeIndex(df['Date']).month == 2) & (pd.DatetimeIndex(df['Date']).day == 29))]
df_2014_2004=df[(df['Date'] > '2003-12-31') & (df['Date'] <= '2014-12-31')]

df_2014_2004.head()


# In[162]:


df_2015 = df[pd.DatetimeIndex(df['Date']).year==2015]
high_2015 = df_2015.groupby('Date', as_index=True)['Data_Value'].agg({"MAX":"max"})

df_2015 = df[pd.DatetimeIndex(df['Date']).year==2015]
low_2015 = df_2015.groupby('Date', as_index=True)['Data_Value'].agg({"MIN":"min"})

high = df_2014_2004.groupby('Date', as_index=True)['Data_Value'].agg({"MAX":"max"})
print(high)

low = df_2014_2004.groupby('Date', as_index=True)['Data_Value'].agg({"MIN":"min"})
print(low)


# In[223]:


plt.figure(figsize=(10,10))

plt.plot(low.index, low['MIN'], low.index, high['MAX'])


# In[224]:


plt.xlabel('Date')
plt.ylabel('Temperature (tenths of degrees C)')
plt.title('Record highest and lowest temperature by day of the year')


# In[225]:


x = plt.gca().xaxis

# rotate the tick labels for the x axis
for item in x.get_ticklabels():
    item.set_rotation(45)
plt.subplots_adjust(bottom=0.45)
plt.gca().fill_between(low.index, low['MIN'], high['MAX'], facecolor='grey', alpha=0.25, label = '_nolegend_')


# In[226]:


record_high2015 = high_2015[high_2015 >= high.reindex_like(high_2015)]
print(record_high2015.head())

x = [n for n in range(0,365) if (high_2015['MAX'].iloc[n] >= high['MAX'].iloc[n]) ]
print(x)

record_low2015 = low_2015[low_2015 <= low.reindex_like(low_2015)]
print(record_low2015.head())

y = [n for n in range(0,365) if (low_2015['MIN'].iloc[n] <= low['MIN'].iloc[n]) ]
print(y)


# In[227]:


plt.scatter(low_2015.index, low_2015, s=10, c='blue')
plt.scatter(high_2015.index, high_2015, s=10, c='red')
plt.legend(['record high', 'record low',
            'record low for 2015', 'record high for 2015'])


# In[229]:


# First let's set the backend without using mpl.use() from the scripting layer
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

# create a new figure
fig = Figure()

# associate fig with the backend
canvas = FigureCanvasAgg(fig)

# add a subplot to the fig
ax = fig.add_subplot(111)

# plot the point (3,2)
ax.plot(3, 2, '.')

# save the figure to test.png
# you can see this figure in your Jupyter workspace afterwards by going to
# https://hub.coursera-notebooks.org/
canvas.print_png('test.png')


# In[ ]:




