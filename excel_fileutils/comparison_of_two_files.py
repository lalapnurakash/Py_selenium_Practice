import pandas as pd

# Load the first Excel file
df1 = pd.read_excel('D:\\s3reports\\UAT.xlsx')

# Load the second Excel file
df2 = pd.read_excel('D:\\s3reports\\prod.xlsx')

# Create an empty DataFrame to store the comparison results
result = pd.DataFrame(columns=['Stock', 'Column', 'Value in Report 1', 'Value in Report 2', 'Match'])

# Loop through each column in the stock reports
for col in df1.columns:
    for i, row in df1.iterrows():
        value1 = row[col]
        value2=""
        value2 = df2.loc[i, col]
        print(k)
        match = value1 == value2

        # Add the comparison result to the result DataFrame
        # result = result.append(
        #     {'Stock': i, 'Column': col, 'Value in Report 1': value1, 'Value in Report 2': value2, 'Match': match},
        #     ignore_index=True)
    result = result.append({'Stock': i,
                            'Column': col,
                            'Value in Report 1': value1, 'Value in Report 2': value2, 'Match': match},
            ignore_index=True)



# Write the comparison results to a new Excel file
df.to_excel('comparison_result.xlsx', index=False)




# Copy the column names from the source worksheet to the new worksheet
# for column in source_worksheet.iter_cols(max_row=1):
#     for cell in column:
#         new_worksheet[cell.coordinate] = cell.value

# Save the new workbook
# Write data to a specific cell using row and column numbers
#worksheet.cell(row=1, column=1, value='Hello, world!')

# Save the changes to the file
#workbook.save('example.xlsx')