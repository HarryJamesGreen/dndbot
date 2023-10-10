import csv

def export_to_csv(text: str, filename: str) -> None:
    """
    Saves the raw OCR output to a CSV file.

    :param text: The extracted text from OCR.
    :param filename: The filename/path of the CSV file.
    """
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([text])