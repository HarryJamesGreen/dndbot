
import pytesseract


def extract_text_from_image(image):
    """
    Extracts text from a given image.

    Parameters:
    - image (Image): Image to extract text from.

    Returns:
    - str: Extracted text.
    """
    text = pytesseract.image_to_string(image, timeout=10)  # Set a 10-second timeout
    return text.strip()