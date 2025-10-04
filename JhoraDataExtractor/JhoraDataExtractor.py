import os
import sys
import csv
import tkinter as tk
from tkinter import filedialog,messagebox

#Global Variables
processed_list = []
files_to_be_processed = []
path = ""
total_files = 0
skipped_files = 0

def AskfilePath():
    global path
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="Select the folder containing your Jhora files (.jhd)")

    if folder_path:

        path = folder_path
        print(f'The folder is set to {path}')
    else:
        messagebox.showwarning(
            title="No Folder Selected",
            message="No folder path was selected. The program will exit."
        )
        sys.exit()

#Validation Check
def valid_check(filepath):
    global total_files
    global skipped_files
    count = 0
    skip_count = 0
    for file in os.listdir(filepath):
        if file.lower().endswith(".jhd"):
            files_to_be_processed.append(file)
            count+=1
        else: 
            skip_count+=1
    total_files = count
    skipped_files = skip_count
    # print(f"{count} valid file(s) found")
    # print(f"{skip_count} invalid file(s) skipped")

'''
# Previews
def file_preview(folder_path):
    count = 0
    print('Top 5 files previews :\n')

    for file in os.listdir(folder_path):
        print(file)
        count += 1
        if count == 5:
            break
    print('\n')
'''

def batch_processor(file_list):
    if len(file_list) <= 0:
        messagebox.showwarning(
            title="No file(s) found",
            message="No file(s) were found with .jhd. The program will exit."
        )
        sys.exit()
    else:
        for file in file_list:
            Data_extractor(file)
        export_to_csv(processed_list)
    
def Data_extractor(file):

    person_name = file.replace('.jhd','')

    open_file = open(os.path.join(path, file))
    line = open_file.readlines()

    data = [str.strip(value) for value in line]
    data.insert(0,person_name)
    open_file.close()

    processed_list.append(data)


def export_to_csv(data):
    global path,total_files,skipped_files 
    filename="1Extracted_details.csv"
    file_path = os.path.join(path, filename)
    header = ["Name", "Month", "Day", "Year", "Time", "Timezone", "Longitude", "Latitude", "Value1", "Value2", "Value3", "Value4", "Value5", "City_Name", "Country", "UnknownVal", "Atmospheric pressure","Temperature", "Gender"]

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    
    messagebox.showinfo(
            title= "Data is extracted successfully",
            message= f"Data is extracted successfully to {path} as {filename} {total_files} files were processed and {skipped_files} other file(s) were skipped"
        )
    sys.exit()

# Main run Script

AskfilePath()
valid_check(path)
# file_preview(path)
batch_processor(files_to_be_processed)