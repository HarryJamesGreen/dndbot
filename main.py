import pytesseract
import logging
import csv
from datetime import datetime

from src.csv_exporter import export_to_csv
from src.Training import perform_ocr_and_annotation
from src.screen_capture import capture_dark_and_darker_window
from src.data_processing import process_ocr_results

# Configure logging
logging.basicConfig(filename='docs/ocr.log', level=logging.INFO)
from logger import setup_logger

logger = setup_logger()

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def save_raw_ocr_to_csv(text, filename):
    """Save the raw OCR extracted text to a CSV file.

    Parameters:
        text (str): The extracted text to save.
        filename (str): The path to the CSV file.
    """
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text])


def main():
    """Main function to execute the OCR processing and data export."""
    perform_training = input('Do you want to perform training? (yes/no): ').strip().lower()
    if perform_training == 'yes':
        for _ in range(3):
            perform_ocr_and_annotation()

    data_to_export = []

    while True:
        screenshot, region = capture_dark_and_darker_window()
        if screenshot:
            screenshot.save("screenshot.png", "PNG")
            try:
                text = pytesseract.image_to_string('screenshot.png')
                print(f"Extracted Text: {text}")

                # Save raw OCR output to CSV
                save_raw_ocr_to_csv(text, 'docs/output.csv')

            except UnicodeDecodeError as e:
                print(f"UnicodeDecodeError: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            print("Processing OCR results...")
            processed_data_list = process_ocr_results(text)

            if processed_data_list is not None:
                data_to_export.extend(processed_data_list)
                export_to_csv(data_to_export, 'docs/processed_data.csv')
            else:
                print("There is nothing to export")


if __name__ == '__main__':
    main()