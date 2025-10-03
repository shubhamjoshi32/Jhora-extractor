import tkinter as tk
from tkinter import filedialog

# Hide the main window
root = tk.Tk()
root.withdraw()

# Open folder selection dialog
folder_path = filedialog.askdirectory(title="Select the folder containing your files")

if folder_path:
    print("You selected:", folder_path)
else:
    print("No folder selected")
