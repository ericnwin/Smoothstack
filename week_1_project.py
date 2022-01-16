# Author: Eric Nguyen

'''
Problem Statement: 
1. Please import csv (or) openpyxl & Logging packages for this problem.
2. Program should take any filename as per the format mentioned as input.
3. Input month value from the file name where  eg :january(expedia_report_monthly_january_2018.xlsx)
4. Based on the month and year input values value print the values in logfile using logger

This is from the first tab :

Eg for January :

Calls Offered: 16,915
Abandon after 30s : 2.32%
FCR : 86.50%
DSAT :  14.20%
CSAT : 78.30%

Similarly go to "VOC Rolling MoM" tab

Grab all the values related to Jan-18 and print.

In Net Promoter Score : Promoters => 200 : good Promoters <200 : bad
			Passives => 100 : good Passives <100 : bad
			Decractors => 100 : good Decrators <100 : bad

Rest all values remain the same.

'''
from datetime import datetime
from openpyxl import load_workbook
import os
import logging

# Creating an instance of logging library
logging.basicConfig(filename=r"C:\Users\Eric\Documents\Python Lessons\SmoothStack\week_1_excel\test.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s: %(message)s")

# Changing directory to the folder where my Excel files are
os.chdir(r'C:\Users\Eric\Documents\Python Lessons\SmoothStack\week_1_excel')

# Listing what's in the folder I selected
lst = os.listdir()
logging.info("Searching all .xls files in week_1_excel folder")
# Retrieve only .xls files (Excel files)
logging.info("Asking user for what file to analyze")
excel_files = [s for s in lst if '.xls' in s]
while(True):
    for index, file in enumerate(excel_files, start=1):
        print(f"{index}. {file}")
    choice = input("\nSelect the number next to the file you'd like: ")
    if choice.isdigit() and int(choice) <= len(excel_files):
        break
    else:
        print("ERROR: You must choose a valid option\n")
        logging.warning("User selected a non-valid option")

excel_file = excel_files[int(choice) - 1]
logging.info(f"User chose {excel_file}")
file_path = os.path.abspath(excel_file)
# print(f"{excel_file}")

# Loading Excel file for file chosen by user
logging.info("Loading Excel File user chose")
wb = load_workbook(file_path)

# Create variables for worksheets 1 and 2
ws_summary = wb.worksheets[0]
ws_voc = wb.worksheets[1]


# Get the 1st element of excel_files and seperate each word + get rid of .xslx extension
print(os.path.splitext(excel_file)[0].split("_"))

# Retrieve Month and Year to filter our data from our excel spreadsheet
logging.info("Grabbing month and year from the file name to filter the data")
month_year = (os.path.splitext(excel_file)[0].split("_"))[-2:]

month_year_split = ' '.join(month_year).title()
print(month_year[0])
month_year_formatted = datetime.strptime(month_year_split, "%B %Y")
print(month_year_formatted)

# Convert string "January 2018" to actual date format
# The cell value is actually a date (1/1/2018) along with a time of 00:00:00, hence the necessity of this step


# print(ws_summary['A'])

worksheet_rows_1st_sheet = list(ws_summary.iter_rows(values_only=True))
worksheet_columns_1st_sheet = list(ws_summary.iter_cols(values_only=True))

for row in worksheet_rows_1st_sheet:
    if row[0] == month_year_formatted:
        row_data = [row for row in row if row != None]
        print(row_data)

# Getting header data
print("Printing header data\n")
header_1st_sheet = []
for col in worksheet_columns_1st_sheet:
    if col[0] != None:
        header_1st_sheet.append(col[0])
print(header_1st_sheet)


worksheet_columns = list(ws_voc.iter_cols(values_only=True))

flag_search_only_month = True
for col in worksheet_columns:
    if col[0] == month_year_formatted:
        col_data = [col for col in col if col != None]
        print(col_data)
        flag_search_only_month = False
    if flag_search_only_month:
        # Will search by getting the month's full name eg. January or March
        if col[0] == month_year[0]:
            print(col)


logging.info(f"Data from {wb.worksheets[0]}")
logging.info(f"{header_1st_sheet[0]}: {row_data[1]}")
for n in range(1, len(header_1st_sheet)):
    logging.info(f"{header_1st_sheet[n].strip()}: {row_data[n+1]:.2%}")

for n in range(1, 7):
    print(f"{col_data[n]}")

if __name__ == "__main__":
    pass
