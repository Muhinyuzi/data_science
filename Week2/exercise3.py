# Let's start with an example and import our graduate admission dataset. First we'll bring in pandas
import pandas as pd
# Then we'll load in our CSV file
df = pd.read_csv('datasets/Admission_Predict.csv', index_col=0)
# And we'll clean up a couple of poorly named columns like we did in a previous lecture
df.columns = [x.lower().strip() for x in df.columns]
# And we'll take a look at the results
print(df.head())
# Boolean masks are created by applying operators directly to the pandas Series or DataFrame objects. 
# For instance, in our graduate admission dataset, we might be interested in seeing only those students 
# that have a chance higher than 0.7
# To build a Boolean mask for this query, we want to project the chance of admit column using the 
# indexing operator and apply the greater than operator with a comparison value of 0.7. This is 
# essentially broadcasting a comparison operator, greater than, with the results being returned as 
# a Boolean Series. The resultant Series is indexed where the value of each cell is either True or False 
# depending on whether a student has a chance of admit higher than 0.7
admit_mask=df['chance of admit'] > 0.7
print(admit_mask.head())
print(type(admit_mask))
# This is pretty fundamental, so take a moment to look at this. The result of broadcasting a comparison
# operator is a Boolean mask - true or false values depending upon the results of the comparison. Underneath,
# pandas is applying the comparison operator you specified through vectorization (so efficiently and in
# parallel) to all of the values in the array you specified which, in this case, is the chance of admit
# column of the dataframe. The result is a series, since only one column is being operator on, filled with
# either True or False values, which is what the comparison operator returns.
# So, what do you do with the boolean mask once you have formed it? Well, you can just lay it on top of the
# data to "hide" the data you don't want, which is represented by all of the False values. We do this by using
# the .where() function on the original DataFrame.
print(df.where(admit_mask).head())
# We see that the resulting data frame keeps the original indexed values, and only data which met 
# the condition was retained. All of the rows which did not meet the condition have NaN data instead,
# but these rows were not dropped from our dataset. 
#
# The next step is, if we don't want the NaN data, we use the dropna() function
print(df.where(admit_mask).dropna().head())
# The returned DataFrame now has all of the NaN rows dropped. Notice the index now includes
# one through four and six, but not five.
#
# Despite being really handy, where() isn't actually used that often. Instead, the pandas devs
# created a shorthand syntax which combines where() and dropna(), doing both at once. And, in
# typical fashion, the just overloaded the indexing operator to do this!
print(df[df['chance of admit'] > 0.7].head())
# I personally find this much harder to read, but it's also very more common when you're reading other
# people's code, so it's important to be able to understand it. Just reviewing this indexing operator on
# DataFrame, it now does two things:
# It can be called with a string parameter to project a single column
print(df["gre score"].head())
# Or you can send it a list of columns as strings
print(df[["gre score","toefl score"]].head())
# And each of these is mimicing functionality from either .loc() or .where().dropna().
# Before we leave this, lets talk about combining multiple boolean masks, such as multiple criteria for
# including. In bitmasking in other places in computer science this is done with "and", if both masks must be
# True for a True value to be in the final mask), or "or" if only one needs to be True.
# Unfortunatly, it doesn't feel quite as natural in pandas. For instance, if you want to take two boolean
# series and and them together
# This doesn't work. And despite using pandas for awhile, I still find I regularly try and do this. The
# problem is that you have series objects, and python underneath doesn't know how to compare two series using
# and or or. Instead, the pandas authors have overwritten the pipe | and ampersand & operators to handle this
# for us
print((df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9))
# One thing to watch out for is order of operations! A common error for new pandas users is
# to try and do boolean comparisons using the & operator but not putting parentheses around
# the individual terms you are interested in
#print(df['chance of admit'] > 0.7 & df['chance of admit'] < 0.9)
# The problem is that Python is trying to bitwise and a 0.7 and a pandas dataframe, when you really want
# to bitwise and the broadcasted dataframes together
# Another way to do this is to just get rid of the comparison operator completely, and instead
# use the built in functions which mimic this approach
print(df['chance of admit'].gt(0.7) & df['chance of admit'].lt(0.9))
# These functions are build right into the Series and DataFrame objects, so you can chain them
# too, which results in the same answer and the use of no visual operators. You can decide what
# looks best for you
df['chance of admit'].gt(0.7).lt(0.9)
# This only works if you operator, such as less than or greater than, is built into the DataFrame, but I
# certainly find that last code example much more readable than one with ampersands and parenthesis.
 # You need to be able to read and write all of these, and understand the implications of the route you are
 # choosing. It's worth really going back and rewatching this lecture to make sure you have it. I would say