import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import logging

logging.basicConfig(filename='ocr.log', level=logging.INFO)

class OCRGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark and Darker market Bot")
        self.root.geometry("600x600")

        # Frame for Image Display
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(padx=10, pady=10, fill="x")

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", length=580)
        self.progress_bar.pack(padx=10, pady=(0, 10), fill="x")

        # Label for Screenshot
        self.image_label = tk.Label(self.image_frame, text="Latest Screenshot:")
        self.image_label.pack(side="left")

        # Canvas for Screenshot
        self.canvas = tk.Canvas(self.image_frame, width=300, height=200, bg="grey", bd=2, relief="groove")
        self.canvas.pack(side="right")

        # Frame for OCR Readings
        self.ocr_frame = tk.Frame(self.root)
        self.ocr_frame.pack(padx=10, pady=10, fill="x")

        # Label for OCR Readings
        self.ocr_label = tk.Label(self.ocr_frame, text="Last 5 OCR Readings:")
        self.ocr_label.pack(side="left")

        # Text Box for OCR Readings
        self.text_box = tk.Text(self.ocr_frame, height=5, width=50, bd=2, relief="groove")
        self.text_box.pack(side="right", fill="x", expand=True)
        self.text_box.insert("1.0", "Most recent 5 data will be displayed here...")

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", length=580)
        self.progress_bar.pack(padx=10, pady=(0, 10), fill="x")

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=10)

    def update_image_with_bounding_box(self, image_with_bounding_box):
        # Update the image on the canvas with bounding box information
        photo = ImageTk.PhotoImage(image_with_bounding_box)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo
    def update_image(self, image_path):
        image = Image.open(image_path)
        image.thumbnail((300, 200))
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def update_text_box_with_csv_data(self, file_path):
        data = self.get_last_5_data_from_csv(file_path)
        self.text_box.delete("1.0", tk.END)
        for row in data:
            self.text_box.insert(tk.END, ', '.join(row) + "\n")

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()


    def clear_text_box(self):
        self.text_box.delete("1.0", tk.END)

    def run(self):
        self.root.mainloop()

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()

    @staticmethod
    def get_last_5_data_from_csv(file_path):
        data = []
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)[-5:]
        except FileNotFoundError:
            logging.warning(f"File not found: {file_path}.")
        except Exception as e:
            logging.error(f"An error occurred while reading {file_path}: {str(e)}")
        return data


if __name__ == '__main__':
    root = tk.Tk()
    gui = OCRGui(root)
    gui.run()
    gui.update_text_box_with_csv_data('processed_data.csv')
    gui.update_image('screenshot_dnd_left_half.png')
