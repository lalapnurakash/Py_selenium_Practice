import time

import pandas as pd
import numpy as np


# data = np.array(['g','e','e'])
# ser = pd.Series(data,index=['name','age','lanh'])
#
# print(ser.iloc[1:2])
#
#
# st="heelloo{}".format('ji')
# st1="he %s".format('uyy')
# print(st1)
# print(st)
# print(ser)
# s="""helloo
# im gndis"""

data= pd.read_csv("D:\\downloads\\nba.csv")
short_data=data.head()
list=[4,4,4,4,4]

short_data["Added values"]= short_data["Salary"].add(list)
#data["Added values"]= data["Salary"].add(other = data['Age'], fill_value = 5)
print(data)
