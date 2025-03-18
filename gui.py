import tkinter as tk
from tkinter import messagebox, filedialog
import logging
from pytubefix import YouTube
from moviepy import *
from pytube.cli import on_progress

logging.basicConfig(
    filename="video_downloader.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


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
            command=self.select_download_directory, highlightthickness=0
        )
        self.canvas.create_window(200, 180, window=self.path_button)

        self.download_button = tk.Button(
            self.root, text="Download", width=30, font=("Helvetica", 12, "bold"),
            command=self.download, highlightthickness=0
        )
        self.canvas.create_window(200, 250, window=self.download_button)

    def select_download_directory(self):
        file_path = filedialog.askdirectory(title="Select Download Directory")
        if file_path:
            logging.info(f"Download directory selected: {file_path}")
            self.path_label.config(text=file_path)
        else:
            logging.info("No download directory was selected.")
            self.path_label.config(text="Select path to download")

    def download(self):
        """
        Download a YouTube video using the provided URL and save it to a user-selected directory.
        """

        video_url = self.url_entry.get()

        download_directory = self.path_label.cget("text").strip()

        if not video_url:
            logging.warning("No video link provided.")
            messagebox.showwarning("Warning", "No video link provided.")
            return

        if not download_directory or download_directory == "Select path to download":
            logging.warning("No valid download directory provided.")
            messagebox.showwarning("Warning", "Please select a valid download directory.")
            return

        try:
            logging.info(f"Starting download for video: {video_url} to directory: {download_directory}")
            yt = YouTube(video_url, on_progress_callback=on_progress)
            stream = yt.streams.get_highest_resolution()

            video_file = stream.download(output_path=download_directory)
            logging.info(f"Video downloaded successfully: {video_file}")

            # Verify the downloaded video file by opening it with moviepy.
            with VideoFileClip(video_file) as video_clip:
                logging.info("Video file processed successfully.")

            messagebox.showinfo("Success", "Video downloaded and processed successfully.")

        except Exception as e:
            logging.error(f"Error downloading video: {e}", exc_info=True)
            messagebox.showerror("Error", f"Error downloading video: {e}")
