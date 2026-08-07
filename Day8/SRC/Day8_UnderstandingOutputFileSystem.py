import os
import openpyxl
def ClearSet():
    input("Pless Enter to continue: ")
    os.system("cls")
while True:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        xcel_path = os.path.abspath(os.path.join(script_dir, "..", "Input"))
        files = os.listdir(xcel_path)
        xlsx_files = [f for f in files if f.endswith(".xlsx")]
        #picking a file that you want to use if more than 1
        if len(xlsx_files) == 1:
            io_file = os.path.join(xcel_path, xlsx_files[0])
        elif len(xlsx_files) == 0:
            print("Error: Missing File. ")
        else:
            file_select = False
            while file_select == False:
                try:
                    print("multiple Excel files found: ")
                    for i, f in enumerate(xlsx_files):
                        print(f"{i+1}. {f}")
                    choise = int(input("Which file? "))
                    io_file = os.path.join(xcel_path, xlsx_files[choise-1])
                    file_select = True
                except:
                    print("Please enter a valid number. ")
                    file_select = False
            ClearSet()
        #Picking which sheets you want to use if more than one.
        wb = openpyxl.load_workbook(io_file)
        sheets = wb.sheetnames
        if len(sheets) == 1:
            ws = wb[sheets[0]]
        elif len(sheets) == 0:
            print("Error: There are no sheets in this excel.")
        else:
            sheet_select = False
            while sheet_select == False:
                try:  
                    print("There are more than 1 sheets in this document. ")
                    for i, f in enumerate(sheets):
                        print(f"{i+1}. {f}")
                    choise = int(input("Which Sheet? "))
                    ws = wb[sheets[choise - 1]]
                    sheet_select = True
                except ValueError:
                    print("Please enter a valid number.")
                    sheet_select = False
        print(f"Sheet: {ws.title}")
        print(f"Max rows: {ws.max_row}")

        header_row = None
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            if row[0] is not None and "Field Tag" in str(row[0]):
                header_row = i
                break

        rows = list(ws.iter_rows(min_row=(header_row + 1), values_only=True))
        headers = rows[0]
        data = rows[1:]
        instruments = []
        for row in data:
            instrument = dict(zip(headers, row))
            instruments.append(instrument)
        print(f"Header found on row: {header_row}")
        print(instruments[0])
        ClearSet()

    except KeyboardInterrupt:
        os.system("cls")
        print("Script cancelled by user.")
        restart = input("Restart? (Y/N): ")
        if restart.lower() != "y":
            break
        ClearSet()