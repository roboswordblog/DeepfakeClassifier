import pandas as pd

df = pd.read_csv('dataset.csv')
# 1 is real 0 is fake

df = df.drop(labels=['label', 'gender', 'category', 'age_group'], axis=1)