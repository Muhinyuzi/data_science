import pandas as pd

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)

import math
print(math.isnan(obj2['California']))

print(obj2['California'] == None)
x = obj2['California']
print(obj2['California'] != x)

import pandas as pd
d = {
    '1': 'Alice',
    '2': 'Bob',
    '3': 'Rita',
    '4': 'Molly',
    '5': 'Ryan'
}
s = pd.Series(d)

print(s.iloc[0:3])

import pandas as pd
s1 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
s2 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})
#print(s2.loc[1])
print(s1.loc[1])
print(s1.iloc[1])
print(s2[1])