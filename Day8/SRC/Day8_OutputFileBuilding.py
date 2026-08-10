import os
import openpyxl

def ClearSet():
    input("Press Enter to continue: ")
    os.system("cls")

# Keep the script running until the user decides to quit.
# Ctrl+C is caught at the bottom and gives the option to restart or exit.
while True:
    try:
        # ── FIND THE INPUT FOLDER ──────────────────────────────────────────
        # Build the path to the Input folder sitting one level above this script.
        # script_dir finds where THIS file lives, then we step up one folder (..)
        # and into the Input folder where the tech drops the IO list.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        xcel_path = os.path.abspath(os.path.join(script_dir, "..", "Input"))

        # Scan the Input folder and collect only .xlsx files.
        files = os.listdir(xcel_path)
        xlsx_files = [f for f in files if f.endswith(".xlsx")]

        # ── SELECT THE IO LIST FILE ────────────────────────────────────────
        # If there's exactly one file, use it automatically.
        # If there are none, tell the tech and stop.
        # If there are multiple, list them and ask which one to use.
        # The while loop keeps asking until they give a valid number.
        if len(xlsx_files) == 1:
            io_file = os.path.join(xcel_path, xlsx_files[0])
        elif len(xlsx_files) == 0:
            print("Error: No Excel file found in the Input folder.")
        else:
            file_select = False
            while file_select == False:
                try:
                    print("Multiple Excel files found:")
                    for file_index, file_name in enumerate(xlsx_files):
                        print(f"{file_index+1}. {file_name}")
                    choice = int(input("Which file? "))
                    io_file = os.path.join(xcel_path, xlsx_files[choice-1])
                    file_select = True
                except:
                    print("Please enter a valid number.")
            ClearSet()

        # ── OPEN THE WORKBOOK AND SELECT A SHEET ──────────────────────────
        # Load the Excel file into memory.
        # Get the list of sheet names, then let the tech pick which one to process.
        # Same pattern as the file selection above.
        wb = openpyxl.load_workbook(io_file)
        sheets = wb.sheetnames

        if len(sheets) == 1:
            ws = wb[sheets[0]]
        elif len(sheets) == 0:
            print("Error: No sheets found in this Excel file.")
        else:
            sheet_select = False
            while sheet_select == False:
                try:
                    print("Multiple sheets found:")
                    for sheet_index, sheet_name in enumerate(sheets):
                        print(f"{sheet_index+1}. {sheet_name}")
                    choice = int(input("Which sheet? "))
                    ws = wb[sheets[choice-1]]
                    sheet_select = True
                except ValueError:
                    print("Please enter a valid number.")

        # ── FIND THE HEADER ROW ────────────────────────────────────────────
        # IO lists have a title section at the top before the real headers start.
        # Instead of hardcoding "row 9", we scan down until we find a row
        # whose first cell contains "Field Tag" — that's our header row.
        # Once found we stop scanning and remember the row number.
        header_row = None
        for row_index, row in enumerate(ws.iter_rows(values_only=True)):
            if row[0] is not None and "Field Tag" in str(row[0]):
                header_row = row_index
                break

        # ── LOAD THE IO DATA INTO A LIST OF DICTIONARIES ──────────────────
        # Start reading from the header row. Row 0 of our slice is the headers,
        # everything after is instrument data.
        # zip() pairs each header with its value in each row,
        # dict() turns those pairs into a dictionary,
        # and we append each instrument dictionary to the instruments list.
        # Result: instruments is a list where each item is one row of the IO list
        # accessible by column name instead of position.
        rows = list(ws.iter_rows(min_row=(header_row + 1), values_only=True))
        headers = rows[0]
        data = rows[1:]
        instruments = []
        for row in data:
            instrument = dict(zip(headers, row))
            instruments.append(instrument)

        print(f"Sheet: {ws.title} | Header on row: {header_row} | Instruments loaded: {len(instruments)}")
        print(instruments[0])
        ClearSet()

    # ── CTRL+C HANDLER ────────────────────────────────────────────────────
    # If the tech presses Ctrl+C at any point, catch it cleanly.
    # Give them the option to restart or exit instead of throwing an error.
    except KeyboardInterrupt:
        os.system("cls")
        print("Script cancelled.")
        restart = input("Restart? (Y/N): ")
        if restart.lower() != "y":
            break
        ClearSet()