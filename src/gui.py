import tkinter as tk
from tkinter import ttk  # Import the ttk module for Treeview

class OCRGui:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Processing Tool")

        # Calculate the center position of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600  # Adjust the window width as needed
        window_height = 400  # Adjust the window height as needed
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window size and position
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a Treeview widget to display the data in a table
        self.tree = ttk.Treeview(self.root, columns=("Data",), show="headings")
        self.tree.heading("Data", text="Processed Data")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Create a Progressbar widget
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x", padx=10, pady=(0, 10))

        # Create a button to perform training
        self.train_button = tk.Button(self.root, text="Train OCR", command=self.perform_ocr_and_annotation)
        self.train_button.pack(pady=10)

    def update_table(self, data):
        # Clear existing rows in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert the processed data into the table if it's not None
        if data is not None:
            for item in data:
                self.tree.insert("", "end", values=(item,))
        else:
            print("Warning: processed_data_list is None.")

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()

    def perform_ocr_and_annotation(self):
        # Implement the OCR and annotation functionality here
        pass

    def run(self):
        # Start the GUI main loop
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    gui = OCRGui(root)
    gui.run()
