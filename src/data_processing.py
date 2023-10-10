import pytesseract
from PIL import Image, ImageStat

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_text_color(img, target_text):
    """Extract the dominant color of the target text from the image.

    Parameters:
        img (PIL.Image): The image to process.
        target_text (str): The text to find in the image.

    Returns:
        tuple: Dominant color of the target text or None if text is not found.
    """
    boxes = pytesseract.image_to_boxes(img)
    for box in boxes.splitlines():
        b = box.split()
        if target_text in b[0]:
            cropped_img = img.crop((int(b[1]), int(b[2]), int(b[3]), int(b[4])))
            dominant_color = ImageStat.Stat(cropped_img).extrema
            return dominant_color
    return None


def process_ocr_results(img):
    """Process OCR results and handle potential errors.

    Parameters:
        img (PIL.Image): The image to process.

    Returns:
        str: Extracted text or cleaned text in case of UnicodeDecodeError.
    """
    try:
        text = pytesseract.image_to_string(img)
        return text
    except UnicodeDecodeError as e:
        print(f'UnicodeDecodeError: {e}')
        cleaned_text = text.encode('utf-8', 'ignore').decode('utf-8')
        return cleaned_text
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None


if __name__ == '__main__':
    # Example usage
    # img = screen_capture.capture_dark_and_darker_window()
    # extracted_data = process_ocr_results(img)
    # csv_exporter.export_to_csv(extracted_data, 'output.csv')
    pass