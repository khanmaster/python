# # This lesson includes
# Introduction to the openpyxl and xlsxwriter libraries
# Using xlsxwriter to create and wrtie to excel files
# Using openpyxl to read from excel files and utilised the data as per the business needs
# Openpyxl and xlsxwriter are standard in python/excel areas and although there are others,
# of which you are free to investigate we will be focusing on this library.

# step 1 -  install openpyxl and xlsxwriter
# click on terminal at the bottom of your pycharm
# type - pip install openpyxl
# type - pip install xlsxwriter

# Note: Throughout XlsxWriter, rows and columns are zero indexed. 
# The first cell in a worksheet, A1 is (0, 0), B1 is (0, 1), A2 is (1, 0), B2 is (1, 1) ..similarly for all.

# Let's create our first file of excel using python
#
# import xlsxwriter
#
# data9 = xlsxwriter.Workbook("data9.xlsx")
#
# worksheet = data9.add_worksheet("Data_9.xlsx")
#
# worksheet.write("A1", "Data 9")
#
#data9.close()

# 5 min challenge - write names of all trainees in our Data 9 class to the excel file just created
# Hint - There are more than one ways of achieve this task,

# Fetch the data from the excel file using python module openpyxl

# import openpyxl
#
# path = "data9.xlsx"
#
# data9_object = openpyxl.load_workbook(path)
#
# data9_sheet = data9_object.active
#
# get_data = data9_sheet.cell(row=1, column=1)
#
# print(get_data.value)

# 5 min challenge - Fetch the data from row3 and column 3 and print
# count the total number of rows and print


# print an active sheet name


# import openpyxl
#
# sheet_name = openpyxl.Workbook()
#
# sheet = sheet_name.active
#
# sheet_title = sheet.title
#
# print("Active sheet title: " + sheet_title)
#
# 5 min challenge -  name the active sheet as Data 9 Team and print
# Hint - You only need to add 1 line of code using one builtin facility of Python
