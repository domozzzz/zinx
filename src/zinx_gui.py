import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from downloader import download_thread

__all__ = ('run_gui')

TITLE = "zinx"
DEFAULT_DESTINATION_PATH = 'C:/'
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.destination_path = DEFAULT_DESTINATION_PATH
        self.init_frame()
        self.init_components()

    def init_frame(self):
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Get entire screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Center window
        x_position = (screen_width // 2) - (WINDOW_WIDTH // 2)
        y_position = (screen_height // 2) - (WINDOW_HEIGHT // 2)
        self.geometry(f"+{x_position}+{y_position}")

    def init_components(self):

        # Source url label
        source_url_label = tk.Label(self, text="Url")
        source_url_label.pack()

        # Source url entry
        source_url_entry = tk.Entry(self, width=40)
        source_url_entry.pack()
        
        def select_destination_path():
            file_path = filedialog.askdirectory()
            if file_path:
                destination_path_label.configure(text=file_path)
                self.destination_path = file_path + "/"

        # Destination path label
        destination_path_label = tk.Label(self, text=DEFAULT_DESTINATION_PATH)
        destination_path_label.pack()

        # Destination path button
        destination_path_button = tk.Button(self, command=select_destination_path)
        destination_path_button.pack()

        # Download button
        download_button = tk.Button(self, text="Download", command=lambda: download_thread(self, source_url_entry.get(), self.destination_path))
        download_button.pack()

        # Progress bar
        self.progress_amount = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=380, mode="determinate", variable=self.progress_amount)
        self.progress_bar.pack(pady=10)

    def update_progress_bar(self, amount):
        self.update_idletasks()  # Update the GUI to reflect the progress
        self.progress_amount.set(amount + 1)

    def set_progress_total(self, total):
        self.progress_bar.configure(maximum=total)

def run_gui():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    run_gui()