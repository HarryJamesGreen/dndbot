import pytesseract

# Configure Tesseract path (Update this path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def test_ocr_on_screenshot(image_path):
    try:
        # Perform OCR on the provided image
        text = pytesseract.image_to_string(image_path)
        print("Extracted Text:")
        print(text)
    except Exception as e:
        print("An error occurred during OCR:")
        print(e)

if __name__ == "__main__":
    # Specify the path to your screenshot image
    screenshot_path = r'C:\Users\coolb\Desktop\New folder (2)\uni\main\Python\Python bot\screenshot.png'

    # Call the test function with the screenshot path
    test_ocr_on_screenshot(screenshot_path)