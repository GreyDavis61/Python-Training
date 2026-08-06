import os
import csv
def clear_set():
    input("please Enter to continue... ")
    os.system("cls")
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample_io_list.csv")
out_path = os.path.join(script_dir, "output.csv")
os.system("cls")

#this will check and see if the CSV file exist where we think it is
if os.path.exists(csv_path):
    print("File Found, Processing. . . ")
else:
    print("Error: IO File not found. Please check the Input folder. ")
clear_set()

#this will check if the file we are looking for is a CSV or not
for file_items in os.listdir(script_dir):
    if file_items.endswith(".csv"):
        print(file_items)
clear_set()

#adds a file to the directory
os.makedirs(os.path.join(script_dir, "PN_Outputs"), exist_ok=True)
print(os.path.basename(csv_path))
clear_set()
#this will break the file name into two parts and  stores them to then print them out
name, ext = os.path.splitext(csv_path)
out_file = name + "_finished" + ext
print(out_file)
clear_set()
#this will check to see if the fil or the directory exists or not (output is "true" or "false")
if os.path.isfile(csv_path):
    print("This file exist! ")
else:
    print("We Don't know where it is. ")
if os.path.isdir(script_dir):
    print("This is a directory! ")
else:
    print("This is not a directory! ")
clear_set()

print(os.path.basename(out_path))
new_path = os.path.join(script_dir, "output_processed.csv")
os.rename(out_path, new_path)
print(os.path.basename(new_path))
clear_set()