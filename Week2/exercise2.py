import pandas as pd

# Pandas mades it easy to turn a CSV into a dataframe, we just call read_csv()
df = pd.read_csv('datasets/Admission_Predict.csv')

# And let's look at the first few rows
df.head()

print(df.head())

# We notice that by default index starts with 0 while the students' serial number starts from 1. If you jump
# back to the CSV output you'll deduce that pandas has create a new index. Instead, we can set the serial no.
# as the index if we want to by using the index_col.

df = pd.read_csv('datasets/Admission_Predict.csv', index_col=0)
df.head()

print(df.head())

# Notice that we have two columns "SOP" and "LOR" and probably not everyone knows what they mean So let's
# change our column names to make it more clear. In Pandas, we can use the rename() function It takes a
# parameter called columns, and we need to pass into a dictionary which the keys are the old column name and
# the value is the corresponding new column name
new_df=df.rename(columns={'GRE Score':'GRE Score', 'TOEFL Score':'TOEFL Score',
                   'University Rating':'University Rating', 
                   'SOP': 'Statement of Purpose','LOR': 'Letter of Recommendation',
                   'CGPA':'CGPA', 'Research':'Research',
                   'Chance of Admit':'Chance of Admit'})
print(new_df.head())

# From the output, we can see that only "SOP" is changed but not "LOR" Why is that? Let's investigate this a
# bit. First we need to make sure we got all the column names correct We can use the columns attribute of
# dataframe to get a list.
print(new_df.columns)
# If we look at the output closely, we can see that there is actually a space right after "LOR" and a space
# right after "Chance of Admit. Sneaky, huh? So this is why our rename dictionary does not work for LOR,
# because the key we used was just three characters, instead of "LOR "
# There are a couple of ways we could address this. One way would be to change a column by including the space
# in the name
new_df=new_df.rename(columns={'LOR ': 'Letter of Recommendation'})
print(new_df.head())
# So that works well, but it's a bit fragile. What if that was a tab instead of a space? Or two spaces?
# Another way is to create some function that does the cleaning and then tell renamed to apply that function
# across all of the data. Python comes with a handy string function to strip white space called "strip()".
# When we pass this in to rename we pass the function as the mapper parameter, and then indicate whether the
# axis should be columns or index (row labels)
new_df=new_df.rename(mapper=str.strip, axis='columns')
# Let's take a look at results
print(new_df.head())
# Now we've got it - both SOP and LOR have been renamed and Chance of Admit has been trimmed up. Remember
# though that the rename function isn't modifying the dataframe. In this case, df is the same as it always
# was, there's just a copy in new_df with the changed names.
print(df.columns)
# We can also use the df.columns attribute by assigning to it a list of column names which will directly
# rename the columns. This will directly modify the original dataframe and is very efficient especially when
# you have a lot of columns and you only want to change a few. This technique is also not affected by subtle
# errors in the column names, a problem that we just encountered. With a list, you can use the list index to
# change a certain value or use list comprehension to change all of the values
# As an example, lets change all of the column names to lower case. First we need to get our list
cols = list(df.columns)
# Then a little list comprehenshion
cols = [x.lower().strip() for x in cols]
# Then we just overwrite what is already in the .columns attribute
df.columns=cols
# And take a look at our results
print(df.head())