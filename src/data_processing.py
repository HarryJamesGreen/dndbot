import pytesseract
from PIL import Image, ImageStat
import logging
import os

# Setup logging
logging.basicConfig(
    filename='ocr_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = os.getenv(
    'TESSERACT_CMD', r'C:\Program Files\Tesseract-OCR\tesseract.exe'
)

def get_text_color(img: Image.Image, target_text: str) -> ImageStat:
    """
    Extracts and returns the dominant color of the text in the image.

    :param img: A PIL Image object.
    :param target_text: Text to find the color for.
    :return: Dominant color of the target text or None if an error occurs.
    """
    try:
        boxes = pytesseract.image_to_boxes(img)
        for box in boxes.splitlines():
            b = box.split()
            if target_text in b[0]:
                cropped_img = img.crop((int(b[1]), int(b[2]), int(b[3]), int(b[4])))
                dominant_color = ImageStat.Stat(cropped_img).extrema
                return dominant_color
        return None
    except Exception as e:
        logging.error("Error in get_text_color: %s", str(e))
        return None

def process_ocr_results(img: Image.Image) -> str:
    """
    Processes the OCR results and handles potential errors.

    :param img: A PIL Image object.
    :return: Extracted text or cleaned text in case of UnicodeDecodeError.
    """
    text = ""
    try:
        text = pytesseract.image_to_string(img)
        return text
    except UnicodeDecodeError as e:
        logging.error('UnicodeDecodeError in process_ocr_results: %s', str(e))
        cleaned_text = text.encode('utf-8', 'ignore').decode('utf-8')
        return cleaned_text
    except Exception as e:
        logging.error('Unexpected error in process_ocr_results: %s', str(e))
        return None
