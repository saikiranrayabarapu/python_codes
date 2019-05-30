import itertools
from itertools import *
a=list(map(int,input().split()))
b=list(map(int,input().split()))
result=itertools.product(a,b)
for each in result:
    print(each,end='')