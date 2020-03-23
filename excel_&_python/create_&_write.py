# Create and write on excel file using xlsxwriter module in Python

# on your terminal run this command - pip install xlsxwriter

# Let's see how to create and write to an excel-sheet


# Note: throughout xlsxwriter, rows and column are zero indexed. The first cell in a worksheet, A1 is (0,0)
# B1 is (0,1), A2 is (1,0) B2 is (1,1) similarly for all ...

# import xlsxwriter module
import xlsxwriter

# workbook() takes one, non-optional, argument
# which is our filename that we want to create.
workbook = xlsxwriter.Workbook("Data9.xlsx")

# Here we have created an object called workbook

# Now we will use to see how to write to our excel sheet using workbook method.

worksheet = workbook.add_worksheet()
# The workbook object is then used to add new work sheet via the add_worksheet() Method.

worksheet.write('A1', "Data 9")
worksheet.write('B1', "Name")
# Now we are using the worksheet object to write/add data via the write() Method.

workbook.close()
# Finally using the close() Method we are saving all the data in the file

# Great! Let's run to see the magic and the power of Python!
# Now when you run this file, Python will create an excel file called Data9 in your current Directory

# Fun time means - very easy exercise
# Please write Name next to Data 9 in the excel file
# Please write profile next to next to name in the excel file
# Please write Job next to profile in the excel file
