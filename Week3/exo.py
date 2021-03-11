import pandas as pd
import numpy as np

df = pd.read_csv("datasets/cwurData.csv")

print(df.head())

print(df.head())
df = df[["institution","score","world_rank"]].dropna()
print(len(df))
df = df[df["score"] <= 100.0]
print(len(df))
print(df.head())

def ranking(x):    
    if x in range(1,101):
        return "First Tier Top University"
    elif x in range(101,201):
        return "Second Tier Top University"
    elif x in range(201,301):
        return "Third Tier Top University"
    else:
        return "Other Top University"

df["Rank_Level"] = df["world_rank"].apply(lambda x: ranking(x))
#print(df)


# With that background, let's see an example of how we would do this in pandas, where we would use the merge
# function.
# First we create two DataFrames, staff and students.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
# And lets index these staff by name
staff_df = staff_df.set_index('Name')
# Now we'll create a student dataframe
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
# And we'll index this by name too
student_df = student_df.set_index('Name')
# And lets just print out the dataframes
print(staff_df.head())
print(student_df.head())
# There's some overlap in these DataFrames in that James and Sally are both students and staff, but Mike and
# Kelly are not. Importantly, both DataFrames are indexed along the value we want to merge them on, which is
# called Name.
# If we want the union of these, we would call merge() passing in the DataFrame on the left and the DataFrame
# on the right and telling merge that we want it to use an outer join. We want to use the left and right
# indices as the joining columns.
merged = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
print(merged)
# We see in the resulting DataFrame that everyone is listed. And since Mike does not have a role, and John
# does not have a school, those cells are listed as missing values.
# If we wanted to get the intersection, that is, just those who are a student AND a staff, we could set the
# how attribute to inner. Again, we set both left and right indices to be true as the joining columns
merged = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
print(merged)
# And we see the resulting DataFrame has only James and Sally in it. Now there are two other common use cases
# when merging DataFrames, and both are examples of what we would call set addition. The first is when we
# would want to get a list of all staff regardless of whether they were students or not. But if they were
# students, we would want to get their student details as well. To do this we would use a left join. It is
# important to note the order of dataframes in this function: the first dataframe is the left dataframe and
# the second is the right
merged = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
print(merged)
# You could probably guess what comes next. We want a list of all of the students and their roles if they were
# also staff. To do this we would do a right join.
merged = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
print(merged)
# We can also do it another way. The merge method has a couple of other interesting parameters. First, you
# don't need to use indices to join on, you can use columns as well. Here's an example. Here we have a
# parameter called "on", and we can assign a column that both dataframe has as the joining column
# First, lets remove our index from both of our dataframes
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
# Now lets merge using the on parameter
merged = pd.merge(staff_df, student_df, how='right', on='Name')
print(merged)
# Using the "on" parameter instead of a the index is how I find myself using merge() the most.
# So what happens when we have conflicts between the DataFrames? Let's take a look by creating new staff and
# student DataFrames that have a location information added to them.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 
                          'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 
                            'Location': '512 Wilson Crescent'}])
# In the staff DataFrame, this is an office location where we can find the staff person. And we can see the
# Director of HR is on State Street, while the two students are on Washington Avenue, and these locations just
# happen to be right outside my window as I film this. But for the student DataFrame, the location information
# is actually their home address.
# The merge function preserves this information, but appends an _x or _y to help differentiate between which
# index went with which column of data. The _x is always the left DataFrame information, and the _y is always
# the right DataFrame information.
# Here, if we want all the staff information regardless of whether they were students or not. But if they were
# students, we would want to get their student details as well.Then we can do a left join and on the column of
# Name
merged = pd.merge(staff_df, student_df, how='left', on='Name')
print(merged)
# From the output, we can see there are columns Location_x and Location_y. Location_x refers to the Location
# column in the left dataframe, which is staff dataframe and Location_y refers to the Location column in the
# right dataframe, which is student dataframe.
# Before we leave merging of DataFrames, let's talk about multi-indexing and multiple columns. It's quite
# possible that the first name for students and staff might overlap, but the last name might not. In this
# case, we use a list of the multiple columns that should be used to join keys from both dataframes on the on
# parameter. Recall that the column name(s) assigned to the on parameter needs to exist in both dataframes.
# Here's an example with some new student and staff data
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 
                          'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 
                          'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 
                          'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 
                            'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 
                            'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 
                            'School': 'Engineering'}])
# As you see here, James Wilde and James Hammond don't match on both keys since they have different last
# names. So we would expect that an inner join doesn't include these individuals in the output, and only Sally
# Brooks will be retained.
merged = pd.merge(staff_df, student_df, how='inner', on=['First Name','Last Name'])
print(merged)