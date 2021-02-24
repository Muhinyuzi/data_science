# Lets import pandas
import pandas as pd
# Pandas is pretty good at detecting missing values directly from underlying data formats, like CSV files.
# Although most missing valuse are often formatted as NaN, NULL, None, or N/A, sometimes missing values are
# not labeled so clearly. For example, I've worked with social scientists who regularly used the value of 99
# in binary categories to indicate a missing value. The pandas read_csv() function has a parameter called
# na_values to let us specify the form of missing values. It allows scalar, string, list, or dictionaries to
# be used.
# Let's load a piece of data from a file called log.csv
df = pd.read_csv('datasets/class_grades.csv')
print(df.head(10))
# We can actually use the function .isnull() to create a boolean mask of the whole dataframe. This effectively
# broadcasts the isnull() function to every cell of data.
mask=df.isnull()
print(mask.head(10))
# This can be useful for processing rows based on certain columns of data. Another useful operation is to be
# able to drop all of those rows which have any missing data, which can be done with the dropna() function.
print(df.dropna().head(10))
# Note how the rows indexed with 2, 3, 7, and 11 are now gone. One of the handy functions that Pandas has for
# working with missing values is the filling function, fillna(). This function takes a number or parameters.
# You could pass in a single value which is called a scalar value to change all of the missing data to one
# value. This isn't really applicable in this case, but it's a pretty common use case.
# So, if we wanted to fill all missing values with 0, we would use fillna
df.fillna(0, inplace=True)
print(df.head(10))
# Note that the inplace attribute causes pandas to fill the values inline and does not return a copy of the
# dataframe, but instead modifies the dataframe you have.
# We can also use the na_filter option to turn off white space filtering, if white space is an actual value of
# interest. But in practice, this is pretty rare. In data without any NAs, passing na_filter=False, can
# improve the performance of reading a large file.
# In addition to rules controlling how missing values might be loaded, it's sometimes useful to consider
# missing values as actually having information. I'll give an example from my own research.  I often deal with
# logs from online learning systems. I've looked at video use in lecture capture systems. In these systems
# it's common for the player for have a heartbeat functionality where playback statistics are sent to the
# server every so often, maybe every 30 seconds. These heartbeats can get big as they can carry the whole
# state of the playback system such as where the video play head is at, where the video size is, which video
# is being rendered to the screen, how loud the volume is.
# If we load the data file log.csv, we can see an example of what this might look like.
df = pd.read_csv("datasets/log.csv")
print(df.head(20))
# In this data the first column is a timestamp in the Unix epoch format. The next column is the user name
# followed by a web page they're visiting and the video that they're playing. Each row of the DataFrame has a
# playback position. And we can see that as the playback position increases by one, the time stamp increases
# by about 30 seconds.
# Except for user Bob. It turns out that Bob has paused his playback so as time increases the playback
# position doesn't change. Note too how difficult it is for us to try and derive this knowledge from the data,
# because it's not sorted by time stamp as one might expect. This is actually not uncommon on systems which
# have a high degree of parallelism. There are a lot of missing values in the paused and volume columns. It's
# not efficient to send this information across the network if it hasn't changed. So this articular system
# just inserts null values into the database if there's no changes.
# Next up is the method parameter(). The two common fill values are ffill and bfill. ffill is for forward
# filling and it updates an na value for a particular cell with the value from the previous row. bfill is
# backward filling, which is the opposite of ffill. It fills the missing values with the next valid value.
# It's important to note that your data needs to be sorted in order for this to have the effect you might
# want. Data which comes from traditional database management systems usually has no order guarantee, just
# like this data. So be careful.
# In Pandas we can sort either by index or by values. Here we'll just promote the time stamp to an index then
# sort on the index.
df = df.set_index('time')
df = df.sort_index()
print(df.head(20))
# If we look closely at the output though we'll notice that the index 
# isn't really unique. Two users seem to be able to use the system at the same 
# time. Again, a very common case. Let's reset the index, and use some 
# multi-level indexing on time AND user together instead,
# promote the user name to a second level of the index to deal with that issue.
df = df.reset_index()
df = df.set_index(['time', 'user'])
print(df)
# Now that we have the data indexed and sorted appropriately, we can fill the missing datas using ffill. It's
# good to remember when dealing with missing values so you can deal with individual columns or sets of columns
# by projecting them. So you don't have to fix all missing values in one command.
df = df.fillna(method='ffill')
print(df.head())
# We can also do customized fill-in to replace values with the replace() function. It allows replacement from
# several approaches: value-to-value, list, dictionary, regex Let's generate a simple example
df = pd.DataFrame({'A': [1, 1, 2, 3, 4],
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
print(df.set_index('A'))
print(df)
# We can replace 1's with 100, let's try the value-to-value approach
print(df.replace(1, 100))
# How about changing two values? Let's try the list approach For example, we want to change 1's to 100 and 3's
# to 300
print(df.replace([1, 3], [100, 300]))
# What's really cool about pandas replacement is that it supports regex too!
# Let's look at our data from the dataset logs again
df = pd.read_csv("datasets/log.csv")
print(df.head(20))
# To replace using a regex we make the first parameter to replace the regex pattern we want to match, the
# second parameter the value we want to emit upon match, and then we pass in a third parameter "regex=True".
# Take a moment to pause this video and think about this problem: imagine we want to detect all html pages in
# the "video" column, lets say that just means they end with ".html", and we want to overwrite that with the
# keyword "webpage". How could we accomplish this?
# Here's my solution, first matching any number of characters then ending in .html
print(df.replace(to_replace=".*.html$", value="webpage", regex=True))
print(df.head(5))











