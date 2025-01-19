import os
import tkinter as tk

root = tk.Tk()
width = root.winfo_screenwidth()

if width != 2560:
    os.system(r"C:\Tools\Windows\Res Switcher\Normal.bat")
else:
    os.system(r"C:\Tools\Windows\Res Switcher\Stretched.bat")

root.destroy()
