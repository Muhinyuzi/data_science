# The set_index() function is a destructive process, and it doesn't keep the current index. 
# If you want to keep the current index, you need to manually create a new column and copy into 
# it values from the index attribute.
# Lets import pandas and our admissions dataset
import pandas as pd
df = pd.read_csv("datasets/Admission_Predict.csv", index_col=0)
print(df.head())
# Let's say that we don't want to index the DataFrame by serial numbers, but instead by the
# chance of admit. But lets assume we want to keep the serial number for later. So, lets
# preserve the serial number into a new column. We can do this using the indexing operator 
# on the string that has the column label. Then we can use the set_index to set index 
# of the column to chance of admit
# So we copy the indexed data into its own column
df['Serial Number'] = df.index
# Then we set the index to another column
df = df.set_index('Chance of Admit ')
print(df.head())
# You'll see that when we create a new index from an existing column the index has a name, 
# which is the original name of the column.
# We can get rid of the index completely by calling the function reset_index(). This promotes the 
# index into a column and creates a default numbered index.
df = df.reset_index()
print(df.head())
# One nice feature of Pandas is multi-level indexing. This is similar to composite keys in 
# relational database systems. To create a multi-level index, we simply call set index and 
# give it a list of columns that we're interested in promoting to an index.
# Pandas will search through these in order, finding the distinct data and form composite indices.
# A good example of this is often found when dealing with geographical data which is sorted by 
# regions or demographics.
# Let's change data sets and look at some census data for a better example. This data is stored in 
# the file census.csv and comes from the United States Census Bureau. In particular, this is a 
# breakdown of the population level data at the US county level. It's a great example of how 
# different kinds of data sets might be formatted when you're trying to clean them.
# Let's import and see what the data looks like
df = pd.read_csv('datasets/census.csv')
print(df.head())
# In this data set there are two summarized levels, one that contains summary 
# data for the whole country. And one that contains summary data for each state.
# I want to see a list of all the unique values in a given column. In this 
# DataFrame, we see that the possible values for the sum level are using the 
# unique function on the DataFrame. This is similar to the SQL distinct operator

# Here we can run unique on the sum level of our current DataFrame 
print(df['SUMLEV'].unique())
# We see that there are only two different values, 40 and 50
# Let's exclue all of the rows that are summaries 
# at the state level and just keep the county data. 
df=df[df['SUMLEV'] == 50]
print(df.head())
# Also while this data set is interesting for a number of different reasons,
# let's reduce the data that we're going to look at to just the total population 
# estimates and the total number of births. We can do this by creating 
# a list of column names that we want to keep then project those and 
# assign the resulting DataFrame to our df variable.
columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012','BIRTHS2013',
                   'BIRTHS2014','BIRTHS2015','POPESTIMATE2010','POPESTIMATE2011',
                   'POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
df = df[columns_to_keep]
print(df.head())
# The US Census data breaks down population estimates by state and county. We can load the data and 
# set the index to be a combination of the state and county values and see how pandas handles it in 
# a DataFrame. We do this by creating a list of the column identifiers we want to have indexed. And then 
# calling set index with this list and assigning the output as appropriate. We see here that we have 
# a dual index, first the state name and second the county name.
df = df.set_index(['STNAME', 'CTYNAME'])
print(df.head())
# An immediate question which comes up is how we can query this DataFrame. We saw previously that 
# the loc attribute of the DataFrame can take multiple arguments. And it could query both the 
# row and the columns. When you use a MultiIndex, you must provide the arguments in order by the 
# level you wish to query. Inside of the index, each column is called a level and the outermost 
# column is level zero. 
# If we want to see the population results from Washtenaw County in Michigan the state, which is 
# where I live, the first argument would be Michigan and the second would be Washtenaw County
print(df.loc['Michigan', 'Washtenaw County'])
# If you are interested in comparing two counties, for example, Washtenaw and Wayne County, we can 
# pass a list of tuples describing the indices we wish to query into loc. Since we have a MultiIndex 
# of two values, the state and the county, we need to provide two values as each element of our 
# filtering list. Each tuple should have two elements, the first element being the first index and 
# the second element being the second index.
# Therefore, in this case, we will have a list of two tuples, in each tuple, the first element is 
# Michigan, and the second element is either Washtenaw County or Wayne County
print(df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ])