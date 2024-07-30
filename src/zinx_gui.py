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
        self.style = ttk.Style(self)
        self.style.theme_use('clam')  # You can choose 'clam', 'alt', 'default', or 'classic'
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
        self.create_source_url_entry()
        self.create_destination_path_selector()
        self.create_download_button()
        self.create_progress_bar()

    def create_source_url_entry(self):
        # Frame for URL entry
        frame = ttk.Frame(self, padding="10 10 10 10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Source url label
        source_url_label = ttk.Label(frame, text="Url")
        source_url_label.grid(row=0, column=0, sticky=tk.W)

        # Source url entry
        self.source_url_entry = ttk.Entry(frame, width=40)
        self.source_url_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
    
    def create_download_button(self):
        download_button = ttk.Button(self, text="Download", command=self.start_download)
        download_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_destination_path_selector(self):
        # Frame for destination path selector
        frame = ttk.Frame(self, padding="10 10 10 10")
        frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # Label
        self.destination_path_label = ttk.Label(frame, text=DEFAULT_DESTINATION_PATH)
        self.destination_path_label.grid(row=0, column=0, sticky=tk.W)

        # Button
        destination_path_button = ttk.Button(frame, text="Select Path", command=self.select_destination_path)
        destination_path_button.grid(row=0, column=1)

    def create_progress_bar(self):
        frame = ttk.Frame(self, padding="10 10 10 10")
        frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

        self.progress_amount = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(frame, orient="horizontal", length=380, mode="determinate", variable=self.progress_amount)
        self.progress_bar.grid(row=0, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

    def select_destination_path(self):
        file_path = filedialog.askdirectory()
        if file_path:
            self.destination_path_label.configure(text=file_path)
            self.destination_path = file_path + "/"

    def start_download(self):
        download_thread(self, self.source_url_entry.get(), self.destination_path)

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
