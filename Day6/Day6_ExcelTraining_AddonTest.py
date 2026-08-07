import os
import csv
import openpyxl
os.system("cls")

def clear_set():
    input("Pless Enter to continue. ")
    os.system("cls")
#this is to find where we are working from, creates a path, then find the corisponding Xcel doc. in a different folder, then creates the path to that folder.
script_dir = os.path.dirname(os.path.abspath(__file__))
xcel_path = os.path.abspath(os.path.join(script_dir, "..", 'Day5'))
io_file = os.path.join(xcel_path, "Platty IO List.xlsx")

#Now we know where the path to the correct Xcel file is, we want to find the "workbook" and "worksheets" we want
wb = openpyxl.load_workbook(io_file)
ws = wb["JB1"]
#This will tell us how many rows and columns we are using in the sheet.
print(ws.max_column)
print(ws.max_row)
clear_set()

#This will print the first 10 rows so we can find the actual title page.
for row in ws.iter_rows(min_row=1, max_row=10, values_only=True):
    print(row)
clear_set()

#We now see that row 9 is the start of the file. let's set the add-on to know this from now on so we don't get confused again
rows = list(ws.iter_rows(min_row=9, values_only=True))
headers = rows[0]    # row 9 - the header
data = rows[1:]      # row 10 onwards - the actual instruments
print(headers)
#Now let's bring that data into the script and store it as a dict. This works like cvs.DictReader but sadly isn't automatic.
instruments = []
for row in data:
    instrument = dict(zip(headers, row))
    instruments.append(instrument)
clear_set()

user_input = input("What PLC tag would you like to look up: ")
user_input = user_input.upper()
found = False
while not found:
    for instrument in instruments:
        if instrument['PLC Tag Name'] and instrument['PLC Tag Name'].upper() == user_input:
            for header, description in instrument.items():
                print(f"{header} | {description}")
            found = True
    if found == False:
        print("Error: Device not found. Check spelling and IO List.")
        user_input = input("Please choose another device: ")
        user_input = user_input.upper()
