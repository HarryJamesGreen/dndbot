from tests.test_speedtest import measure_execution_time
from src.text_extraction import extract_text_from_image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# speedtest for function extract_text_from_image
def test_csv_exporter():
    for i in range(5):
        sample_file = 'captured_dark_and_darker.png'
        # Measure execution time with sample file
        execution_time = measure_execution_time(extract_text_from_image, sample_file)
        print(f'Execution time for extract_text_from_image: {execution_time:.4f} seconds')

def main():
    test_csv_exporter()

if __name__ == '__main__':
    main()
