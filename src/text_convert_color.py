import cv2
import pytesseract
from statistics import mode

def extract_text_and_color_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    results = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y:y+h, x:x+w]
        pixels = roi.reshape((-1, 3))
        dominant_color = mode(map(tuple, pixels))
        text = pytesseract.image_to_string(roi)
        results.append({
            'text': text.strip(),
            'color': dominant_color
        })

    return results