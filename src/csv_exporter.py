import csv
def export_to_csv(data, filename="output.csv"):
    """
    Exports given data to a CSV file.

    Parameters:
    - data (list of lists): Data to be exported.
    - filename (str): Name of the CSV file.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)