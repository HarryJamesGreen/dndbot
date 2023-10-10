import pytest
from src.data_processing import process_ocr_results
import pytest

from src.data_processing import process_ocr_results


@pytest.fixture
def readable_csv_file(tmp_path):
    # Create a temporary CSV file with some data
    file_path = tmp_path / "test_data.csv"
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Column1", "Column2"])
        writer.writerow(["Data1", "Data2"])

    return file_path

def test_process_ocr_results(readable_csv_file):
    # Call the process_ocr_results function with the path of the readable CSV file
    existing_data = process_ocr_results(str(readable_csv_file))

    # Assert that the result is a list
    assert isinstance(existing_data, list)

    # Assert that the list contains the expected data
    expected_data = [["Column1", "Column2"], ["Data1", "Data2"]]
    assert existing_data == expected_data

if __name__ == '__main__':
    pytest.main()

import csv

file_path = r'C:\Users\coolb\Desktop\New folder (2)\uni\main\Python\Python bot\docs\processed_data.csv'

try:
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        existing_data = [row for row in reader]
        print("File read successfully!")
except Exception as e:
    print(f"Error reading file: {str(e)}")
