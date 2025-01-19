import os
import tkinter as tk

root = tk.Tk()
width = root.winfo_screenwidth()

if width != 2560:
    os.system(r"C:\Tools\Windows\ResSwitcher\Normal.bat")
    print("normal")
else:
    os.system(r"C:\Tools\Windows\ResSwitcher\Stretched.bat")
    print("stretched")

root.destroy()
