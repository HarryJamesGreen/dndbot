from src.screen_capture import capture_screen
from src.text_extraction import extract_text_from_image
from src.csv_exporter import export_to_csv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust the path accordingly


def main():
    # Define the region to capture (adjust these values as needed)
    region = (100, 100, 300, 300)

    # Capture the screen region
    screenshot = capture_screen(region)

    # Extract text from the screenshot
    text = extract_text_from_image(screenshot)

    # For demonstration, let's assume each line in the text is a separate data entry
    data = text.splitlines()

    # Export the data to a CSV file
    export_to_csv(data)


if __name__ == "__main__":
    main()
