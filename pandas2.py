import pandas as pd

man = ['Charming','Handsome','Smart','Brillient','Humble']

s = pd.Series(man)

print(s.values)

print(s.index)

print(s.dtype)

print(s)