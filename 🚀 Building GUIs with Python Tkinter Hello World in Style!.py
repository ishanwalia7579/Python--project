import tkinter as tk
from tkinter import font

root = tk.Tk()
label = tk.Label(root, text="Hello World!", font=("Arial", 20))  # Font size 20
label.pack()
root.mainloop()
