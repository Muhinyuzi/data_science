# -*- coding: utf-8 -*-
#Splitting
# Let's look at an example. First, we'll bring in our pandas and numpy libraries
import pandas as pd
import numpy as np
import timeit
# Let's look at some US census data
df = pd.read_csv('datasets/census.csv')
# And exclude state level summarizations, which have sum level value of 40
df = df[df['SUMLEV']==50]
print(df.head())
# In the first example for groupby() I want to use the census data. Let's get a list of the unique states,
# then we can iterate over all the states and for each state we reduce the data frame and calculate the
# average.
# Let's run such task for 3 times and time it. For this we'll use the cell magic function %%timeit
#%%timeit -n 3
for state in df['STNAME'].unique():
    # We'll just calculate the average using numpy for this particular state
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    # And we'll print it to the screen
    print('Counties in state ' + state + 
          ' have an average population of ' + str(avg))
#4.62 s ± 230 ms per loop (mean ± std. dev. of 7 runs, 3 loops each)
# If you scroll down to the bottom of that output you can see it takes a fair bit of time to finish.
# Now let's try another approach using groupby()
#%%timeit -n 3
# For this method, we start by telling pandas we're interested in grouping by state name, this is the "split"
for group, frame in df.groupby('STNAME'):
    # You'll notice there are two values we set here. groupby() returns a tuple, where the first value is the
    # value of the key we were trying to group by, in this case a specific state name, and the second one is
    # projected dataframe that was found for that group
    # Now we include our logic in the "apply" step, which is to calculate an average of the census2010pop
    avg = np.average(frame['CENSUS2010POP'])
    # And print the results
    print('Counties in state ' + group + 
          ' have an average population of ' + str(avg))
# And we don't have to worry about the combine step in this case, because all of our data transformation is
# actually printing out results. 
#29.6 ms ± 3.65 ms per loop (mean ± std. dev. of 7 runs, 3 loops each)
# Wow, what a huge difference in speed. An improve by roughly by two factors!
# Now, 99% of the time, you'll use group by on one or more columns. But you can also provide a function to
# group by and use that to segment your data.
# This is a bit of a fabricated example but lets say that you have a big batch job with lots of processing and
# you want to work on only a third or so of the states at a given time. We could create some function which
# returns a number between zero and two based on the first character of the state name. Then we can tell group
# by to use this function to split up our data frame. It's important to note that in order to do this you need
# to set the index of the data frame to be the column that you want to group by first.
# We'll create some new function called set_batch_number and if the first letter of the parameter is a capital
# M we'll return a 0. If it's a capital Q we'll return a 1 and otherwise we'll return a 2. Then we'll pass
# this function to the data frame
df = df.set_index('STNAME')
def set_batch_number(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2
# The dataframe is supposed to be grouped by according to the batch number And we will loop through each batch
# group
for group, frame in df.groupby(set_batch_number):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')
#There are 1177 records in group 0 for processing.
#There are 1134 records in group 1 for processing.
#There are 831 records in group 2 for processing.
# Notice that this time I didn't pass in a column name to groupby(). Instead, I set the index of the dataframe
# to be STNAME, and if no column identifier is passed groupby() will automatically use the index.
# Let's take one more look at an example of how we might group data. In this example, I want to use a dataset
# of housing from airbnb. In this dataset there are two columns of interest, one is the cancellation_policy
# and the other is the review_scores_value.
df=pd.read_csv("datasets/listings.csv")
print(df.head())
# So, how would I group by both of these columns? A first approach might be to promote them to a multiindex
# and just call groupby()
df=df.set_index(["cancellation_policy","review_scores_value"])
# When we have a multiindex we need to pass in the levels we are interested in grouping by
for group, frame in df.groupby(level=(0,1)):
    print(group)
# This seems to work ok. But what if we wanted to group by the cancelation policy and review scores, but
# separate out all the 10's from those under ten? In this case, we could use a function to manage the
# groupings
def grouping_fun(item):
    # Check the "review_scores_value" portion of the index. item is in the format of
    # (cancellation_policy,review_scores_value
    if item[1] == 10.0:
        return (item[0],"10.0")
    else:
        return (item[0],"not 10.0")
for group, frame in df.groupby(by=grouping_fun):
    print(group)
print(df.head())   
#Applying
# To this point we have applied very simple processing to our data after splitting, really just outputting
# some print statements to demonstrate how the splitting works. The pandas developers have three broad
# categories of data processing to happen during the apply step, Aggregation of group data, Transformation of
# group data, and Filtration of group data
#Aggregation
# The most straight forward apply step is the aggregation of data, and uses the method agg() on the groupby
# object. Thus far we have only iterated through the groupby object, unpacking it into a label (the group
# name) and a dataframe. But with agg we can pass in a dictionary of the columns we are interested in
# aggregating along with the function we are looking to apply to aggregate.
# Let's reset the index for our airbnb data
df=df.reset_index()
# Now lets group by the cancellation policy and find the average review_scores_value by group
print(df.groupby("cancellation_policy").agg({"review_scores_value":np.average}))
# Hrm. That didn't seem to work at all. Just a bunch of not a numbers. The issue is actually in the function
# that we sent to aggregate. np.average does not ignore nans! However, there is a function we can use for this
print(df.groupby("cancellation_policy").agg({"review_scores_value":np.nanmean}))
# We can just extend this dictionary to aggregate by multiple functions or multiple columns.
print(df.groupby("cancellation_policy").agg({"review_scores_value":(np.nanmean,np.nanstd),
                                      "reviews_per_month":np.nanmean}))

# Take a moment to make sure you understand the previous cell, since it's somewhat complex. First we're doing
# a group by on the dataframe object by the column "cancellation_policy". This creates a new GroupBy object.
# Then we are invoking the agg() function on that object. The agg function is going to apply one or more
# functions we specify to the group dataframes and return a single row per dataframe/group. When we called
# this function we sent it two dictionary entries, each with the key indicating which column we wanted
# functions applied to. For the first column we actually supplied a tuple of two functions. Note that these
# are not function invocations, like np.nanmean(), or function names, like "nanmean" they are references to
# functions which will return single values. The groupby object will recognize the tuple and call each
# function in order on the same column. The results will be in a heirarchical index, but since they are
# columns they don't show as an index per se. Then we indicated another column and a single function we wanted
# to run.
#Transformation
# Transformation is different from aggregation. Where agg() returns a single value per column, so one row per
# group, tranform() returns an object that is the same size as the group. Essentially, it broadcasts the
# function you supply over the grouped dataframe, returning a new dataframe. This makes combining data later
# easy.
# For instance, suppose we want to include the average rating values in a given group by cancellation policy,
# but preserve the dataframe shape so that we could generate a difference between an individual observation
# and the sum.
# First, lets define just some subset of columns we are interested in
cols=['cancellation_policy','review_scores_value']
# Now lets transform it, I'll store this in its own dataframe
transform_df=df[cols].groupby('cancellation_policy').transform(np.nanmean)
print(transform_df.head())
# So we can see that the index here is actually the same as the original dataframe. So lets just join this
# in. Before we do that, lets rename the column in the transformed version
transform_df.rename({'review_scores_value':'mean_review_scores'}, axis='columns', inplace=True)
df=df.merge(transform_df, left_index=True, right_index=True)
df.head()
# Great, we can see that our new column is in place, the mean_review_scores. So now we could create, for
# instance, the difference between a given row and it's group (the cancellation policy) means.
df['mean_diff']=np.absolute(df['review_scores_value']-df['mean_review_scores'])
df['mean_diff'].head()
#Filtering
# The GroupBy object has build in support for filtering groups as well. It's often that you'll want to group
# by some feature, then make some transformation to the groups, then drop certain groups as part of your
# cleaning routines. The filter() function takes in a function which it applies to each group dataframe and
# returns either a True or a False, depending upon whether that group should be included in the results.
# For instance, if we only want those groups which have a mean rating above 9 included in our results
df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value'])>9.2)
# Notice that the results are still indexed, but that any of the results which were in a group with a mean
# review score of less than or equal to 9.2 were not copied over.
#Applying
# By far the most common operation I invoke on groupby objects is the apply() function. This allows you to
# apply an arbitrary function to each group, and stitch the results back for each apply() into a single
# dataframe where the index is preserved.
# Lets look at an example using our airbnb data, I'm going to get a clean copy of the dataframe
df=pd.read_csv("datasets/listings.csv")
# And lets just include some of the columns we were interested in previously
df=df[['cancellation_policy','review_scores_value']]
df.head()
# In previous work we wanted to find the average review score of a listing and its deviation from the group
# mean. This was a two step process, first we used transform() on the groupby object and then we had to
# broadcast to create a new column. With apply() we could wrap this logic in one place
def calc_mean_review_scores(group):
    # group is a dataframe just of whatever we have grouped by, e.g. cancellation policy, so we can treat
    # this as the complete dataframe
    avg=np.nanmean(group["review_scores_value"])
    # now broadcast our formula and create a new column
    group["review_scores_mean"]=np.abs(avg-group["review_scores_value"])
    return group
# Now just apply this to the groups
df.groupby('cancellation_policy').apply(calc_mean_review_scores).head()
# Using apply can be slower than using some of the specialized functions, especially agg(). But, if your
# dataframes are not huge, it's a solid general purpose approach