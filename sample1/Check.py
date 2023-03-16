import copy
import random
import  matplotlib.pyplot as plt
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains

org=[1,3,54]
#cpy=org
#cpy[1]=10
copyord=copy.copy(org)
obe=copy.deepcopy(copyord)
copyord[0]=11
copylist=list(org)
copywith =org[:]
print(org)
print(copyord)
print(copylist)
print(copywith)

import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
    else:
        print('Start')

# importing pandas as pd

# Creating the Series
sr = pd.Series([10, 25, 3, 11, 24, 6])

# Create the Index
index_ = ['Coca Cola', 'Sprite', 'Coke', 'Fanta', 'Dew', 'ThumbsUp']

# set the index
sr.index = index_

# replace 3 by 1000
result = sr.replace(to_replace = 3, value = 1000)

# Print the series
print(result)
r1=sr.reset_index()

# making data frame from csv file
data = pd.read_csv("D:\\downloads\\employees.csv")

# setting first name as index column
data.set_index("First Name", inplace=False)

# display
print(data.head())




# converting and overwriting values in column
data["First Name"] = data["First Name"].str.lower()
print(data)
sam=int(random.random())
print(sam)
nums = []
low = 10
high = 100
mode = 20

for i in range(10000):
    temp = random.triangular(low, high, mode)
    nums.append(temp)

# plotting a graph
plt.hist(nums, bins=200)
plt.show()
print(random.randint(3, 9))
nums = []
alpha = 3

for i in range(100):
    temp = random.betavariate(1,10)
    nums.append(temp)

# plotting a graph
plt.plot(nums)
plt.show()


# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
       'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)