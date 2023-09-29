import pytesseract
import time

def extract_text_from_image(image, timeout=10):
    try:
        start_time = time.time()

        while time.time() - start_time < timeout:
            text = pytesseract.image_to_string(image)
            if text.strip():
                return text

        # Handle timeout
        print("OCR process timed out.")
        return ""

    except Exception as e:
        print(f"Error during OCR: {str(e)}")
        return ""
