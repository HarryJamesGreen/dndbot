import os
import csv


def export_to_csv(data, csv_filename):
    # Extract directory from the filename
    directory = os.path.dirname(csv_filename)

    # Check if the directory exists, if not, create it
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(csv_filename, mode='w', newline='') as file:
        fieldnames = ['timestamp', 'name', 'item', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)
