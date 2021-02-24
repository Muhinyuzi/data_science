import csv
import os
import sys
import datetime as dt
import time as tm



with open("datasets/mpg.csv") as csvfile:
    mpg = list(csv.DictReader(csvfile))

print(mpg[:3]) # The first three dictionaries in our list.
print(len(mpg))# `len` shows that our list is comprised of 234 dictionaries.   
print(mpg[0].keys())
average_cty = sum(float(d['cty']) for d in mpg) / len(mpg)
print("The average cty fuel economy across all cars is: {}".format(average_cty))
average_hwy = sum(float(d['hwy']) for d in mpg) / len(mpg)
print("The average hwy fuel economy across all cars is: {}".format(average_hwy))
#Use `set` to return the unique values for the number of cylinders the cars in our dataset have.
#set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set. 
cylinders = set(d['cyl'] for d in mpg)
print('The different numbers of cylinders in all cars {}.'.format(cylinders))
#Here's a more complex example where we are grouping the cars by number of cylinder, and finding the average cty mpg for each group.
CtyMpgByCyl = []
for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')
CtyMpgByCyl.sort(key=lambda x: x[0])
print('The average cty mpg by cylinder group is: {}'.format(CtyMpgByCyl))

#Use `set` to return the unique values for the class types in our dataset.
vehicleclass = set(d['class'] for d in mpg) # what are the class types
print('Different classes of vehicles are {}.'.format(vehicleclass))

#And here's an example of how to find the average hwy mpg for each class of vehicle in our dataset.
HwyMpgByClass = []
for e in vehicleclass:
	summpg = 0
	classtypecount = 0
	for d in mpg:
		if d['class'] == e:
			summpg += float(d['hwy'])
			classtypecount += 1
	HwyMpgByClass.append((e, summpg / classtypecount)) # append the tuple ('class', 'avg mpg')
HwyMpgByClass.sort(key=lambda x: x[1])
print('The average hwy mpg by class group is: {}'.format(HwyMpgByClass))


#`time` returns the current time in seconds since the Epoch. (January 1st, 1970)
print(tm.time())
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)

#`timedelta` is a duration expressing the difference between two dates.
delta = dt.timedelta(days = 100) # create a timedelta of 100 days
print(delta)





