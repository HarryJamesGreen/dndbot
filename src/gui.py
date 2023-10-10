import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import logging

# Configure logging
logging.basicConfig(filename='ocr.log', level=logging.INFO)


class OCRGui:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Processing Tool")

        # Set the window size and position
        self.root.geometry("600x600")

        # Create a Canvas widget to display the screenshot
        self.canvas = tk.Canvas(self.root, width=300, height=200)
        self.canvas.pack(padx=10, pady=10)

        # Create a Treeview widget to display the data in a table
        self.tree = ttk.Treeview(self.root, columns=("Data",), show="headings")
        self.tree.heading("Data", text="Processed Data")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Create a Text widget to display the last 5 data exported to CSV
        self.text_box = tk.Text(self.root, height=5, width=50)
        self.text_box.pack(padx=10, pady=10)
        self.text_box.insert("1.0", "Most recent 5 data will be displayed here...")

        # Create a Progressbar widget
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x", padx=10, pady=(0, 10))

        # Update the button to exit the application
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=10)

    def update_image(self, image_path):
        # Open the image and convert it to Tkinter PhotoImage
        image = Image.open(image_path)
        image.thumbnail((300, 200))
        photo = ImageTk.PhotoImage(image)

        # Add the image to the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo  # Keep a reference to avoid garbage collection

    def update_text_box_with_csv_data(self, file_path):
        """
        Update the Text Widget with the last 5 data from the CSV file.

        Parameters:
            file_path (str): The path to the CSV file.
        """
        data = self.get_last_5_data_from_csv(file_path)

        # Clear the text box
        self.text_box.delete("1.0", tk.END)

        # Insert the last 5 data into the text box
        for row in data:
            self.text_box.insert(tk.END, ', '.join(row) + "\n")

    def update_table(self, data):
        # Clear existing rows in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert the processed data into the table if it's not None
        if data is not None:
            for item in data:
                self.tree.insert("", "end", values=(item,))
        else:
            return  # Return if data is None

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()

    def run(self):
        # Start the GUI main loop
        self.root.mainloop()

    @staticmethod
    def get_last_5_data_from_csv(file_path):
        """
        Get the last 5 rows from the CSV file.

        Parameters:
            file_path (str): The path to the CSV file.

        Returns:
            list: A list of the last 5 rows from the CSV file.
        """
        data = []
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)[-5:]  # Get the last 5 rows
        except FileNotFoundError:
            logging.warning(f"File not found: {file_path}.")
        except Exception as e:
            logging.error(f"An error occurred while reading {file_path}: {str(e)}")

        return data


if __name__ == '__main__':
    root = tk.Tk()
    gui = OCRGui(root)
    gui.run()

    # Example usage: Update the Text Widget with the last 5 data from the CSV file
    gui.update_text_box_with_csv_data('docs/processed_data.csv')
    gui.update_image('docs/screenshot.png')
