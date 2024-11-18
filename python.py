import csv

# Open and read the CSV file
file_path = "D:\\COMPLETE_B.TECH_C.S.E\\7th_SEMESTER\\MINOR PROJECT\\Project\\DATA.csv"

# Open the CSV file for reading
with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    
    # Print each row in the CSV file
    for row in reader:
        print(row)
