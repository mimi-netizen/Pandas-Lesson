import pandas as pd 

'''
s1 = pd.Series([1,2,30,50,45,8,55,70]) # Direct method
print(s1)
'''

'''
lst = ['Ali', 'John', 'Luka']
s2 = pd.Series(lst) # From a list
print(s2)  
'''

'''
tpl = ['Ali', 'John', 'Luka']
s3 = pd.Series(tpl) # From a Tuple
print(s3)
'''

'''
st = {'Ali', 'John', 'Luka'}
new_st = list(st)
s4 = pd.Series(new_st) # From a SET
print(s4)
'''

dic = {'Name':"Ali", "Age":20}
s5 = pd.Series(dic) # From a Dictionary
print(s5)