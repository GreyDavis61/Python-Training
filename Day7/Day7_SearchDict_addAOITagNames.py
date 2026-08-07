import os
import openpyxl
os.system("cls")

def clear_set():
    input("Press Enter to continue")
    os.system("cls")

script_dir = os.path.dirname(os.path.abspath(__file__))
xcel_path = os.path.abspath(os.path.join(script_dir, "..", "Day5"))
io_file = os.path.join(xcel_path, "Platty IO List.xlsx")

wb = openpyxl.load_workbook(io_file)
ws = wb["JB1"]
rows = list(ws.iter_rows(min_row=9, values_only=True))
headers = rows[0]
data = rows[1:]
instruments = []
for row in data:
    instrument = dict(zip(headers, row))
    instruments.append(instrument)

io_attributes = {
    "AI":  ["PV", "InUse", "BadPVAlarm", "HSD", "HiHiAlarm", "HiAlarm", "LoAlarm", "LoLoAlarm", "LSD"],
    "AIH": ["PV", "InUse", "BadPVAlarm", "HSD", "HiHiAlarm", "HiAlarm", "LoAlarm", "LoLoAlarm", "LSD"],
    "DI":  ["Value", "InUse", "Alarm", "Shutdown"],
    "DO":  ["Value", "InUse", "Raw",],
    "AO":  ["CV", "Cfg_IncToClose", "InUse", ],
    "RTD": ["PV", "InUse", "BadPVAlarm", "HSD", "HiHiAlarm", "HiAlarm", "LoAlarm", "LoLoAlarm", "LSD"]
}
for aoi_tag in instruments:
    if aoi_tag['IO Status'] == "Standard IO":
        io_type = aoi_tag['I/O Type']
        attribute = io_attributes[io_type]
        for tags in attribute:
            print(f"{aoi_tag['PLC Tag Name']}.{tags}")
        clear_set()
            

    