from itertools import *
import itertools
l=[]
string,s=input().split()
k=int(s)
for i in string:
    l.append(i)
result=itertools.permutations(sorted(l),k)
separator=''
for each in result:
    print(separator.join(each))
