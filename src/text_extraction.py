from PIL import Image
import pytesseract

def extract_text_from_image(image):
    """
    Extracts text from a given image.

    Parameters:
    - image (Image): Image to extract text from.

    Returns:
    - str: Extracted text.
    """
    text = pytesseract.image_to_string(image)
    return text.strip()
