Python GUI Downloader
This is a simple GUI downloader application built with Python's Tkinter library and the requests module. It allows users to download files from a given URL and save them to a specified location on their computer.

Features:-
   i) User-friendly Interface: A simple graphical interface for easy interaction.

  ii) URL Input: Enter the URL of the file you want to download.

  iii) Browse and Save: Choose where to save the downloaded file using a file dialog.

  iv) Progress Bar: Monitor the download progress with a visual progress bar.

  v) Automatic Filename Suggestion: Automatically suggests a filename based on the URL.

Getting Started
  Prerequisites
  Python 3.x installed on your system.

Installation
  Clone the repository (or download main.py):

Bash
git clone <repository_url>
cd <repository_directory>
(Replace <repository_url> and <repository_directory> with the actual values if this project is hosted on GitHub.)

Install the required libraries:

Bash

pip install requests
Usage
Run the application:

Bash

python main.py
Enter the URL: In the "ENter URL" field, paste the direct URL of the file you wish to download.

Browse for save location (Optional): Click the "Browser" button to choose a different location and filename for your download. If you don't select a location, the file will be saved in the same directory as the script with a filename derived from the URL.

Start Download: Click the "Download" button to begin the download process. The progress bar will update as the file downloads.

rhead.py (Additional Script)
The rhead.py script is a separate utility that demonstrates how to use IP proxies with the requests library. It's not directly integrated into the GUI downloader but can be used independently for testing proxy functionality.

Note: The rhead.py script uses placeholder values for proxies ("http": "", "https": ""). You would need to replace these with actual proxy server addresses and ports to use it effectively (e.g., using a service like Asocks as indicated in the comments).

To run rhead.py:

Bash

python rhead.py
This will print your public IP address as seen by the target server, potentially through a proxy if configured correctly.
