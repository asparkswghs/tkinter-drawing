#!/usr/bin/env python
import tkinter as tk
import sys

# Functions
def draw():
    """ Draw the Line on the Canvas """
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
    except ValueError:
        return

    canvas.create_line(x1, y1, x2, y2)

def draw_auto():
    for i in range(1, 20):
        canvas.create_line(1, 1, 1000, 1000*i)

def clear():
    """ Clear the canvas """
    canvas.delete("all")

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
label_x1 = tk.Label(window, text="x₁ = ")
label_y1 = tk.Label(window, text="y₁ = ")
label_x2 = tk.Label(window, text="x₂ = ")
label_y2 = tk.Label(window, text="y₂ = ")

# Define Entry Boxes
entry_x1 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
entry_y1 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
entry_x2 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))
entry_y2 = tk.Entry(window, validate='all', validatecommand=(call_validate, '%P'))

# Define Buttons
button = tk.Button(window, text="Draw!", command = draw)
button_clear = tk.Button(window, text="Clear", command = clear)

# Canvases
canvas = tk.Canvas(window)

# Append to Grid
label_x1.grid(column=0, row=0)
label_y1.grid(column=0, row=1)
label_x2.grid(column=0, row=2)
label_y2.grid(column=0, row=3)

entry_x1.grid(column=1, row=0)
entry_y1.grid(column=1, row=1)
entry_x2.grid(column=1, row=2)
entry_y2.grid(column=1, row=3)

button.grid(column=1, row=4, pady=5, padx=10)
button_clear.grid(column=3, row=4)

canvas.grid(column=0, row=5, columnspan=2)

# Present Window
window.mainloop()
