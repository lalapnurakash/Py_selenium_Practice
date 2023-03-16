import openpyxl
from openpyxl import load_workbook
import openpyxl.reader.excel
import xlrd

wb= xlrd.open_workbook("files///Book1.xlsx")
sheet = wb.sheet_by_name("Sheet1")
rows = sheet.nrows
print(rows)
print(sheet.cell_value(0, 0))
for i in range(rows):
    print(sheet.cell_value(i, 1))

