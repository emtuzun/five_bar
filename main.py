import tkinter as tk
from tkinter import ttk
import math

# drawing arms function
def draw_arms():
    canvas.delete("all")
    line = canvas.create_line(0, 250, 500, 250, dash=(3,1))
    arm_dis = float(arm_dis_var.get())
    arm_len1 = float(arm_len1_var.get())
    arm_len2 = float(arm_len2_var.get())
    angle1 = float(angle1_var.get())
    angle2 = float(angle2_var.get())
    x_1 = 250-(arm_dis/2)+arm_len1*math.cos(math.radians(angle1))
    y_1 = 250-arm_len1*math.sin(math.radians(angle1))
    x_2 = 250+(arm_dis/2)+arm_len1*math.cos(math.radians(angle2))
    y_2 = 250-arm_len1*math.sin(math.radians(angle2))
    d = math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2)/2
    x_3 = ((x_1+x_2) / 2) - ((y_2-y_1) * math.sqrt(4*(arm_len2**2) - d**2)) / (2*d)
    y_3 = ((y_1+y_2) / 2) - ((x_2-x_1) * math.sqrt(4*(arm_len2**2) - d**2)) / (2*d)
    arm1 = canvas.create_line(250-(arm_dis/2), 250, x_1, y_1)
    arm2 = canvas.create_line(x_1, y_1, x_3, y_3)
    arm3 = canvas.create_line(250+(arm_dis/2), 250, x_2, y_2)
    arm4 = canvas.create_line(x_2, y_2, x_3, y_3)
    canvas.grid(column=0, row=6, columnspan=2)
root = tk.Tk()
root.title("Five Bars")
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=900)

arm_dis_var = tk.StringVar()
arm_len1_var = tk.StringVar()
arm_len2_var = tk.StringVar()
angle1_var = tk.StringVar()
angle2_var = tk.StringVar()

arm_dis_label = ttk.Label( root, text="Arm Distance")
arm_len1_label = ttk.Label( root, text="Arm Length 1")
arm_len2_label = ttk.Label( root, text="Arm Length 2")
angle1_label = ttk.Label( root, text="Angle 1")
angle2_label = ttk.Label( root, text="Angle 2")

arm_dis_entry = ttk.Entry( root, textvariable = arm_dis_var)
arm_len1_entry = ttk.Entry( root, textvariable = arm_len1_var)
arm_len2_entry = ttk.Entry( root, textvariable = arm_len2_var)
angle1_entry = ttk.Entry( root, textvariable = angle1_var)
angle2_entry = ttk.Entry( root, textvariable = angle2_var)

sub_btn=tk.Button(root, text = 'Olustur', command = draw_arms)


content.grid(column=0, row=0)
arm_dis_label.grid(column=0, row=0)
arm_dis_entry.grid(column=1, row=0)
arm_len1_label.grid(column=0, row=1)
arm_len1_entry.grid(column=1, row=1)
arm_len2_label.grid(column=0, row=2)
arm_len2_entry.grid(column=1, row=2)
angle1_label.grid(column=0, row=3)
angle1_entry.grid(column=1, row=3)
angle2_label.grid(column=0, row=4)
angle2_entry.grid(column=1, row=4)
sub_btn.grid(column=0, row=5, columnspan=2)

canvas = tk.Canvas(root, bg="red", height=500, width=500)
line = canvas.create_line(0, 250, 500, 250, dash=(3,1))
canvas.grid(column=0, row=6, columnspan=2)
root.mainloop()