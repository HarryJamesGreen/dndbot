import pytesseract
from src.data_processing import process_ocr_results
# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def test_ocr():
    try:
        text = pytesseract.image_to_string("test_screenshot.png")
        print("Extracted Text:", text)
    except Exception as e:
        print("OCR Error:", str(e))

test_ocr()



def test_data_processing():
    extracted_text = "Your extracted text here"
    screenshot_path = "test_screenshot.png"
    csv_file_path = 'processed_data.txt'

    processed_data_list = process_ocr_results(extracted_text, screenshot_path, csv_file_path)
    print("Processed Data List:", processed_data_list)


test_data_processing()

