import os
import csv
import pytest

@pytest.mark.parametrize("file_path", [
    r'C:\Users\coolb\Desktop\New folder (2)\uni\main\Python\Python bot\docs\processed_data.csv',
    # Add more file paths to test here
])
def test_file_readability(file_path):
    try:
        # Check if the file exists
        assert os.path.exists(file_path), f"File does not exist: {file_path}"

        # Check if the file is readable
        assert os.access(file_path, os.R_OK), f"File is not readable: {file_path}"

        # Try to read the file
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            existing_data = [row for row in reader]
            print("\nFile read successfully!")


    except Exception as e:
        pytest.fail(f"Error reading file {file_path}: {str(e)}")

# Usage
if __name__ == '__main__':
    pytest.main()
