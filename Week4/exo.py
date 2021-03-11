import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv('datasets/grades.csv')

print(df.head())
early_finishers = df[df['assignment1_submission'] > '2016']
print(early_finishers.head())
late_finishers = df[df['assignment1_submission'] <= '2016']
print(late_finishers.head())

print(ttest_ind(early_finishers['assignment1_grade'], late_finishers['assignment1_grade']))