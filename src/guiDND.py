import tkinter as tk
from PIL import Image, ImageTk
import logging
import pytesseract

# Configure Tesseract and logging
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
logging.basicConfig(filename="ocr.log", level=logging.INFO)


class OCRGui:
    def __init__(self, master=None):
        self.root = master
        self.root.title("Dark and Darker market Bot")
        self.root.geometry("600x600")

        # Initialize canvas and ensure it's packed or placed in the layout
        self.canvas = tk.Canvas(self.root, width=300, height=200)
        self.canvas.pack()

        # [Optional] You might want to initialize an empty image to avoid any issues with updating later
        self.update_image("path_to_a_default_image.jpg")

    def update_image(self, image_path):
        try:
            image = Image.open(image_path)
            image.thumbnail((300, 200))
            photo = ImageTk.PhotoImage(image)

            # Check if an image is already displayed on the canvas
            if hasattr(self, "canvas_image"):
                self.canvas.delete(self.canvas_image)

            self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo  # Keep a reference to avoid garbage collection
        except FileNotFoundError:
            logging.warning(f"Image file not found: {image_path}.")
        except Exception as e:
            logging.error(f"An error occurred while updating image: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    gui = OCRGui(root)
    root.mainloop()
