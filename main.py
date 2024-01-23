#!/usr/bin/env python
import tkinter as tk

# Functions

def validate(P):
    """ Validates Entry boxes, to only contain int """
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

# Window Properties
window = tk.Tk()
window.title("Drawing")
window.geometry("600x400")
window.minsize(300, 200)

call_validate = window.register(validate)

# Define Labels
label_x1 = tk.Label(window, text="X 1 = ")
label_x2 = tk.Label(window, text="X 2 = ")
label_y1 = tk.Label(window, text="Y 1 = ")
label_y2 = tk.Label(window, text="Y 2 = ")

# Define Entry Boxes
entry_x1 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
entry_x2 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
entry_y1 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
entry_y2 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))

# Canvases


# Append to Grid
label_x1.grid(column=0, row=0)
label_x2.grid(column=0, row=1)
label_y1.grid(column=0, row=2)
label_y2.grid(column=0, row=3)

entry_x1.grid(column=1, row=0)
entry_x2.grid(column=1, row=1)
entry_y1.grid(column=1, row=2)
entry_y2.grid(column=1, row=3)

# Present Window
window.mainloop()
