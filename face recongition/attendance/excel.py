import openpyxl
from openpyxl import workbook,load_workbook
book = load_workbook('excel.xlsx')
sheet = book.active

print(sheet)