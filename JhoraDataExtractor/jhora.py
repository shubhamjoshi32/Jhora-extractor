import os
import csv

#Global Variables
processed_list = []
files_to_be_processed = []
path = "C:/Users/Shubham/Desktop/Astro Jhora"

#Validation Check
def valid_check(filepath):
    count = 0
    skip_count = 0
    for file in os.listdir(filepath):
        if file.lower().endswith(".jhd"):
            files_to_be_processed.append(file)
            count+=1
        else: 
            skip_count+=1
    print(f"{count} valid file(s) found")
    print(f"{skip_count} invalid file(s) skipped")

#Previews
def file_preview(folder_path):
    count = 0
    print('Top 5 files previews :\n')

    for file in os.listdir(folder_path):
        print(file)
        count += 1
        if count == 5:
            break
    print('\n')

def batch_processor(file_list):
    for file in file_list:
        Data_extractor(file)
    export_to_csv(processed_list)
    
def Data_extractor(file):

    person_name = file.replace('.jhd','')
    
    open_file = open(f"{path}/{file}")

    line = open_file.readlines()

    data = [str.strip(value) for value in line]
    data.insert(0,person_name)

    open_file.close()

    processed_list.append(data)

def export_to_csv(data):
    filename="Extracted_details.csv"
    header = ["Name", "Month", "Day", "Year", "Time", "Timezone", "Longitude", "Latitude", "Value1", "Value2", "Value3", "Value4", "Value5", "City_Name", "Country", "UnknownVal", "Atmospheric pressure","Temperature", "Gender"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    print(f"CSV saved as {filename}")


# Main run Script

valid_check(path)
file_preview(path)
batch_processor(files_to_be_processed)