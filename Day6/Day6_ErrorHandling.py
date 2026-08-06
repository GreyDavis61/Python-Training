import os
import csv
def clear_set():
    input("Pless enter to continue. ")
    os.system("cls")
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample_io_list.csv")

os.system("cls")

try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}. Good Work! ")
except ValueError:
    print("That wasn't a number. ")
except KeyboardInterrupt:
    print("User cancelled. ")
clear_set()

try:
    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Status'] == 'Standard IO':
                print(row['Field_Tag'])
except FileNotFoundError:
    print("Error: IO list not found. Please check the Input Folder. ")
except KeyError as key_error_code:
    print(f"Error: Missing column in IO List: {key_error_code}")
finally:
    print("Done. ")
    clear_set()