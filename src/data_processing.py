import pytesseract
from PIL import Image, ImageStat
import logging
import os
import csv
import re

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

def process_ocr_results(text):
    # Regular expression to extract timestamp, username, and message
    pattern = re.compile(r'\[(.*?)\] (.*?) : (.*)')

    # Find all matches in the OCR text
    matches = pattern.findall(text)

    # Save matches to CSV
    with open('docs/processed_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for match in matches:
            writer.writerow(match)
