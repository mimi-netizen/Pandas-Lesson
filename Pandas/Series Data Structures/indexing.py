import pandas as pd

s = pd.Series([4,67,3,90,52,6348], index=['A','B','C','D','E','F'])
print(s.loc['A']) # loc[], #iloc[]