import numpy as np
import pandas as pd

a = np.arange(8)
b = a[4:6]
b[:] = 40
c = a[4] + a[6]
print(c)

import re
s = 'ABCAC'
print(bool(re.match('A', s))==True)

print(re.match('A', s) == True)

print(bool(re.match('A', s)) == True)

def result():
    s = 'ACAABAACAAABACDBADDDFSDDDFFSSSASDAFAAACBAAAFASD'

    result = []
    # compete the pattern below
    pattern = "([^A])(A{3})"
    for item in re.finditer(pattern, s):
      # identify the group number below.
      result.append(item.group(1))
      
    return result
print(result())  

df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])
print(df)
print(df.index[0])
#print(df[0])

S = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print('Check')
print(S['b':'e'])
print(S[['b', 'c', 'd']])
print(S[S <= 3][S > 0])
print(S[1:4])

print(df.index[0])
print(df.iloc[0])

students_scores = {'d': 4,
'b': 7,
'a': -5,'c': 3}
df1 = pd.Series(students_scores)
print('Here')
print(df1)
print(df1['d'])
print(df1.iloc[0])
print(df1.index[0])
print(df1[0])


s1_1 = {'Mango': 20,
'Strawberry': 15,
'Blueberry': 18,
'Vanilla': 31}
s2_2 = {'Strawberry': 20,
'Vanilla': 30,
'Banana': 15,
'Mango': 20,
'Plain': 20}

s1 = pd.Series(s1_1)
s2 = pd.Series(s2_2)
s3 = s1.add(s2)

print(s3)
print(s3['Plain'] >= s3['Mango'])
print(s3['Blueberry'] == s1.add(s2, fill_value = 0)['Blueberry'])
print(s3['Mango'] >=  s1.add(s2, fill_value = 0)['Mango'])#answer
print(s3['Blueberry'] == s1['Blueberry'])

import numpy as np

a = np.arange(8)
b = a[4:6]
b[:] = 40
c = a[4] + a[6]
print(c)




