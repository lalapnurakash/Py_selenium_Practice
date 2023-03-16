import pandas as pd

# read the two Excel files into dataframes
df1=pd.read_excel('D:\\s3reports\\UAT.xlsx')

df2=pd.read_excel('D:\\s3reports\\prod.xlsx')



# get the maximum number of rows from both dataframes
max_rows = max(len(df1), len(df2))

# add missing rows to the existing dataframe with default value 'N/A'
df = df1.reindex(range(max_rows), fill_value='N/A')

# write the updated dataframe to the Excel file
df.to_excel('existing_file.xlsx', index=False)