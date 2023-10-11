import tkinter as tk

class DndBotGUI(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self, text="Start", command=self.start_processing)
        self.start_button.pack(side="top")

    def start_processing(self):
        print("Start button was pressed")
        # Implement the logic you want to execute when the Start button is pressed

def main():
    root = tk.Tk()
    root.title("DnD Bot")  # Set the title here
    root.geometry("800x600")  # Set the geometry here
    app = DndBotGUI(master=root)
    app.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
