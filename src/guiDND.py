import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import logging
import pytesseract
import src.data_processing as dp
logging.basicConfig(filename="ocr.log", level=logging.INFO)


class OCRGui:
    def __init__(self, master=None):
        self.root = root
        self.root.title("Dark and Darker market Bot")
        self.root.geometry("600x600")
        self.setup_gui_elements()

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

    def update_text_box_with_csv_data(self, file_path):
        data = self.get_last_5_data_from_csv(file_path)
        self.text_box.delete("1.0", tk.END)
        for row in data:
            self.text_box.insert(tk.END, ", ".join(row) + "\n")

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()

    def clear_text_box(self):
        self.text_box.delete("1.0", tk.END)

    def run(self):
        self.root.mainloop()
        # Consider placing method calls here if they should execute when the GUI is running

    @staticmethod
    def get_last_5_data_from_csv(file_path):
        data = []
        try:
            with open(file_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                data = list(reader)[-5:]
        except FileNotFoundError:
            logging.warning(f"File not found: {file_path}.")
        except Exception as e:
            logging.error(f"An error occurred while reading {file_path}: {str(e)}")
        return data


if __name__ == "__main__":
    root = tk.Tk()
    gui = OCRGui(root)
    gui.run()
        # If there are method calls that should execute when the GUI is running, consider placing them in a method inside OCRGui
