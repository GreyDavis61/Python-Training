import os
import csv

os.system("cls")
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample_io_list.csv")

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)
    with open(os.path.join(script_dir, "output.csv"), "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Field_Tag", "PLC_Tag", "IO_Type", "Description"])
        for row in reader:
            if row['Status'] == "Standard IO":
                writer.writerow([row['Field_Tag'], row['PLC_Tag'], row['IO_Type'], row['Description']])