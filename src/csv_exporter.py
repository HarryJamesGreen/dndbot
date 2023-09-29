import csv

def export_to_csv(data, filename="output.csv"):
    with open(filename, 'a', newline='') as file:  # 'a' mode for appending
        writer = csv.writer(file)
        writer.writerows(data)