from os.path import isfile,join
import os

list=[f for f in os.listdir('/Users') if isfile(join('/1003633',f))]
print(list)
print(os.listdir('/Users/1003633'))
