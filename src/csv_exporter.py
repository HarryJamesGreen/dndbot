import csv

def export_to_csv(data, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        fieldnames = ['timestamp', 'name', 'item', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)