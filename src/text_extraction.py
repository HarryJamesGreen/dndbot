import pytesseract
from statistics import mode
import cv2

def extract_text_and_color_from_image(image):
    text = pytesseract.image_to_string(image, timeout=10).strip()

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape((-1, 3))
    dominant_color = mode(map(tuple, pixels))

    return text, dominant_color