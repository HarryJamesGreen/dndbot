
import csv

def export_to_csv(data, headers, filename="output.csv"):
    """
    Exports given data to a CSV file.

    Parameters:
    - data (list of lists): Data to be exported.
    - headers (list): Headers for the CSV.
    - filename (str): Name of the CSV file.
    """
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)