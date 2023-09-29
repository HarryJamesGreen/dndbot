import re
import pytesseract
from PIL import Image, ImageStat
from src import screen_capture, csv_exporter
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

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


def process_ocr_results(img):
    results = []
    text = ""  # Initialize text to an empty string
    pattern = r'\[(\d{2}:\d{2}:\d{2}[AM|PM]{2})\] \(([^)]+)\) : ([^:]+): (\d{4}G)'  # Define pattern outside the try block

    try:
        text = pytesseract.image_to_string(img)
        matches = re.findall(pattern, text)

        for match in matches:
            timestamp, name, item, gold = match
            color = get_text_color(img, item)
            results.append({'timestamp': timestamp, 'name': name, 'item': item, 'price': gold, 'color': color})

    except UnicodeDecodeError:
        # Handle the UnicodeDecodeError by cleaning the text
        cleaned_text = text.encode('utf-8', 'ignore').decode('utf-8')
        matches = re.findall(pattern, cleaned_text)

        for match in matches:
            timestamp, name, item, gold = match
            color = get_text_color(img, item)
            results.append({'timestamp': timestamp, 'name': name, 'item': item, 'price': gold, 'color': color})

    except Exception as e:
        print(f"Error during OCR: {e}")

    return results


if __name__ == '__main__':
    img = screen_capture.capture_dark_and_darker_window()
    extracted_data = process_ocr_results(img)
    csv_exporter.export_to_csv(extracted_data, 'output.csv')
