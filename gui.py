import tkinter as tk


class GUI:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Video Downloader")
        self.root.geometry("500x400")
        self.root.config(padx=10, pady=10)

        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        self.app_label = tk.Label(self.root, text="Video Downloader", fg="blue", font=("Arial", 30))
        self.canvas.create_window(200, 20, window=self.app_label)

        self.url_label = tk.Label(self.root, text="Enter video URL", font=("Arial", 15))
        self.canvas.create_window(200, 80, window=self.url_label)

        self.url_entry = tk.Entry(self.root, width=60)
        self.canvas.create_window(200, 100, window=self.url_entry)

        self.path_label = tk.Label(self.root, text="Select path to download", font=("Arial", 15))
        self.canvas.create_window(200, 150, window=self.path_label)

        self.path_button = tk.Button(
            self.root, text="Select", width=30, font=("Helvetica", 12, "bold"),
            command="", highlightthickness=0
        )
        self.canvas.create_window(200, 180, window=self.path_button)

        self.download_button = tk.Button(
            self.root, text="Download", width=30, font=("Helvetica", 12, "bold"),
            command="", highlightthickness=0
        )
        self.canvas.create_window(200, 250, window=self.download_button)
