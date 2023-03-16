import pandas as pd
import numpy as np

df1=pd.read_excel('D:\\s3reports\\UAT.xlsx')

df2=pd.read_excel('D:\\s3reports\\prod.xlsx')

#diff=df1.compare(df2,align_axis=1)
#difference = df1[df1!=df2]
#print (difference)
# print(diff)
#print(df1.merge(df2, indicator=False,how='outer').assign(_merge=lambda x:x!='both'))
# # print(df1.shape)
# comparison_values=df1.values==df2.values
# rows, cols = np.where(comparison_values == False)
# for item in zip(rows, cols):
# df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])
