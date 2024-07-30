import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from downloader import download_thread

__all__ = ('run_gui')

TITLE = "zinx"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200

DEFAULT_DESTINATION_FOLDER = 'C:/'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.destination_folder = DEFAULT_DESTINATION_FOLDER
        self.screen_init()

    def screen_init(self):
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width // 2) - (WINDOW_WIDTH // 2)
        y_position = (screen_height // 2) - (WINDOW_HEIGHT // 2)

        self.geometry(f"+{x_position}+{y_position}")

        input_label = tk.Label(self, text="Url")
        input_label.pack()

        entry = tk.Entry(self, width=40)
        entry.pack()
        
        def choose_folder_location():
            file_path = filedialog.askdirectory()
            if file_path:
                folder_location_label.configure(text=file_path)
                self.folder_location = file_path + "/"

        folder_location_label = tk.Label(self, text=DEFAULT_DESTINATION_FOLDER)
        folder_location_label.pack()

        folder_location_button = tk.Button(self, command=choose_folder_location)
        folder_location_button.pack()

        submit_button = tk.Button(self, text="Download", command=lambda: download_thread(self, entry.get(), self.folder_location))
        submit_button.pack()

        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(self, orient="horizontal", length=380, mode="determinate", variable=self.progress_var)
        self.progress.pack(pady=10)

    def print_progress(self, i):
        self.update_idletasks()  # Update the GUI to reflect the progress
        self.progress_var.set(i+1)

    def set_total(self, total):
        self.progress.configure(maximum=total)

def run_gui():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    run_gui()