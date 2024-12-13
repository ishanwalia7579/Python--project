import tkinter as tk
from time import strftime

def update_time():
    """Update the clock label with the current time."""
    current_time = strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)
    return False

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Configure the clock label
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
clock_label.pack(anchor='center', pady=20)

# Start the clock
update_time()

# Run the application
root.mainloop()
