import pandas as pd

cities = pd.read_html('https://oadbnmpl.labs.coursera.org/files/assignments/assignment4/assets/wikipedia_data.html')[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
print(cities.head())