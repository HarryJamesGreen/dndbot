from src.csv_exporter import export_to_csv
from src.screen_capture import capture_dark_and_darker_window
from src.data_processing import remove_duplicates_from_list
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def main():
    data_to_export = []

    while True:
            # Capture the specified region
            screenshot = capture_dark_and_darker_window()
            if screenshot:
                screenshot.save("screenshot.png")
            else:
                print("Failed to capture the screenshot.")

            # Try to extract text from the screenshot
            try:
                text = pytesseract.image_to_string(screenshot)
                time.sleep(2)
            except Exception as e:
                print(f"Error extracting text: {e}")
                continue  # Skip the current iteration and continue with the next
            print(text)
            # Append the extracted text to data_to_export
            for line in text.splitlines():
                data_to_export.append([line])

            # Export the data to the CSV file
            data = [1, 2, 2, 3, 4, 4, 5]
            unique_data = remove_duplicates_from_list(data)
            export_to_csv(data_to_export)
            time.sleep(2)


if __name__ == "__main__":
    main()
