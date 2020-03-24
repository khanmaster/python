#  Using the row-column notation(indexing value) for writing data in the specific cells.

# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('data_team.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. 
# Rows and columns are zero indexed. 
row = 0
column = 0

content = ["Andy", "Ben", "CJ", "Khan", "Isabella", "Sparta Global", "London"]

# iterating through content list 
for item in content:
    # write operation perform
    worksheet.write(row, column, item)

    # incrementing the value of row by one 
    # with each iteratons. 
    row += 1

workbook.close()