import re
import pytesseract
from PIL import Image, ImageStat
from src import screen_capture, csv_exporter
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'


#   Error Handling

def get_text_color(img, target_text):
    boxes = pytesseract.image_to_boxes(img)
    for box in boxes.splitlines():
        b = box.split()
        if target_text in b[0]:
            cropped_img = img.crop((int(b[1]), int(b[2]), int(b[3]), int(b[4])))
            dominant_color = ImageStat.Stat(cropped_img).extrema
            return dominant_color
    return None


import re
from pytesseract import pytesseract

import re
from pytesseract import pytesseract

import re
from pytesseract import pytesseract


import traceback

def process_ocr_results(img):
    text = ""  # Initialize text to an empty string
    try:
        text = pytesseract.image_to_string(img)
        # rest of your code...
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        cleaned_text = text.encode('utf-8', 'ignore').decode('utf-8')
        # rest of your code using cleaned_text...
    except Exception as e:
        print(f"you are an indiot: {e}")
        # Handle or log other exceptions...
    return None  # or return an appropriate value





if __name__ == '__main__':
    img = screen_capture.capture_dark_and_darker_window()
    extracted_data = process_ocr_results(img)
    csv_exporter.export_to_csv(extracted_data, 'output.csv')
