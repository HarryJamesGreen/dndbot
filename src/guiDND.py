import tkinter as tk
from PIL import Image, ImageTk
import logging
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

logging.basicConfig(filename="ocr.log", level=logging.INFO)

class OCRGui:
    def __init__(self, master=None):
        self.root = master  # Corrected reference to master
        self.root.title("Dark and Darker market Bot")
        self.root.geometry("600x600")


    def update_image(self, image_path):
        try:
            image = Image.open(image_path)
            image.thumbnail((300, 200))
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo
        except FileNotFoundError:
            logging.warning(f"Image file not found: {image_path}.")
        except Exception as e:
            logging.error(f"An error occurred while updating image: {str(e)}")

    # ... Rest of the class remains unchanged

if __name__ == "__main__":
    root = tk.Tk()
    gui = OCRGui(root)
    root.mainloop()
    # Method calls that should execute when the GUI is running should be placed inside a method in OCRGui
