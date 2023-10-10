import csv

file_path = r'C:\Users\coolb\Desktop\New folder (2)\uni\main\Python\Python bot\docs\processed_data.csv'

try:
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        existing_data = [row for row in reader]
        print("File read successfully!")
except Exception as e:
    print(f"Error reading file: {str(e)}")