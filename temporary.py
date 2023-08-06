from tkinter import *

root = Tk()

def callback(event):
    print("clicked at", event.x, event.y)

canvas= Canvas(root, width=100, height=100)
canvas.bind("<Button-1>", callback)
canvas.pack()

root.mainloop()