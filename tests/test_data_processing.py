import os
import pytest
from src.data_processing import process_ocr_results

@pytest.fixture
def readable_csv_file():
    # Calculate the path to the CSV file based on the project structure
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    csv_file_path = os.path.join(project_root, 'docs', 'processed_data.csv')
    return csv_file_path

def test_process_ocr_results(readable_csv_file):
    # Ensure the CSV file exists
    assert os.path.exists(readable_csv_file)

    # Test process_ocr_results function
    # You can provide sample OCR text as input for testing
    sample_ocr_text = "[timestamp] username : [item](x1) 10g"
    process_ocr_results(sample_ocr_text)
