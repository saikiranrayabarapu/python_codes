import itertools
from itertools import *
lover_boy=['prasad','poorna','kiran','satish']
is_love=[True,True,False,True]
result=itertools.compress(lover_boy,is_love)
for each in result:
    print(each)