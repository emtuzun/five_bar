import tkinter as tk
from tkinter import ttk
import math
import time

# calculating angles


def calculate_angles():
    a = float(arm_dis_var.get())
    k = float(arm_len1_var.get())
    l = float(arm_len2_var.get())
    x_1 = float(pos1_x_var.get())
    y_1 = float(pos1_y_var.get())
    x_2 = float(pos2_x_var.get())
    y_2 = float(pos2_y_var.get())

    b = math.sqrt(y_1**2 + (x_1-a/2)**2)
    c = math.sqrt(y_1**2 + (x_1+a/2)**2)
    alpha_1 = math.acos((a**2 + b**2 - c**2)/(2*a*b))
    alpha_2 = math.acos((k**2 + b**2 - l**2)/(2*k*b))
    beta_1 = math.acos((a**2 + c**2 - b**2)/(2*a*c))
    beta_2 = math.acos((k**2 + c**2 - l**2)/(2*k*c))
    angle1 = beta_1+beta_2
    angle2 = math.pi - (alpha_1 + alpha_2)
    if (y_1 < 0):
        angle1 = -angle1
        angle2 = -angle2

    b = math.sqrt(y_2**2 + (x_2-a/2)**2)
    c = math.sqrt(y_2**2 + (x_2+a/2)**2)
    alpha_1 = math.acos((a**2 + b**2 - c**2)/(2*a*b))
    alpha_2 = math.acos((k**2 + b**2 - l**2)/(2*k*b))
    beta_1 = math.acos((a**2 + c**2 - b**2)/(2*a*c))
    beta_2 = math.acos((k**2 + c**2 - l**2)/(2*k*c))
    angle3 = beta_1+beta_2
    angle4 = math.pi - (alpha_1 + alpha_2)
    if (y_2 < 0):
        angle3 = -angle3
        angle4 = -angle4
    print(math.degrees(angle1))
    print(math.degrees(angle2))
    print(math.degrees(angle3))
    print(math.degrees(angle4))
# drawing arms function


def move_arms(arm_dis: float, arm_len1: float, arm_len2: float, angle1: float, angle2: float):
    x_1 = 250-(arm_dis/2)+arm_len1*math.cos(math.radians(angle1))
    y_1 = 250-arm_len1*math.sin(math.radians(angle1))
    x_2 = 250+(arm_dis/2)+arm_len1*math.cos(math.radians(angle2))
    y_2 = 250-arm_len1*math.sin(math.radians(angle2))
    d = math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2)
    h = math.sqrt(arm_len2**2 - (d/2)**2)
    x_3 = ((x_1+x_2) / 2) + (h*(y_2-y_1))/d
    y_3 = ((y_1+y_2) / 2) - (h*(x_2-x_1))/d
    canvas.delete("all")
    canvas.create_line(0, 250, 500, 250, dash=(3, 1))
    canvas.create_line(250-(arm_dis/2), 250, x_1, y_1)
    canvas.create_line(x_1, y_1, x_3, y_3)
    canvas.create_line(250+(arm_dis/2), 250, x_2, y_2)
    canvas.create_line(x_2, y_2, x_3, y_3)


def draw_arms():
    arm_dis = float(arm_dis_var.get())
    arm_len1 = float(arm_len1_var.get())
    arm_len2 = float(arm_len2_var.get())
    angle1 = float(angle1_var.get())
    angle2 = float(angle2_var.get())
    angle3 = float(angle3_var.get())
    angle4 = float(angle4_var.get())
    n = 100
    for i in range(n):
        move_arms(arm_dis, arm_len1, arm_len2, angle1 +
                  ((angle3-angle1)/n)*i, angle2+((angle4-angle2)/n)*i)
        time.sleep(0.01)
        root.update()


root = tk.Tk()
root.title("Five Bars")

arm_dis_var = tk.StringVar()
arm_len1_var = tk.StringVar()
arm_len2_var = tk.StringVar()
angle1_var = tk.StringVar()
angle2_var = tk.StringVar()
angle3_var = tk.StringVar()
angle4_var = tk.StringVar()
pos1_x_var = tk.StringVar()
pos1_y_var = tk.StringVar()
pos2_x_var = tk.StringVar()
pos2_y_var = tk.StringVar()

arm_dis_label = ttk.Label(root, text="Arm Distance")
arm_len1_label = ttk.Label(root, text="Arm Length 1")
arm_len2_label = ttk.Label(root, text="Arm Length 2")
angle1_label = ttk.Label(root, text="Angle 1")
angle2_label = ttk.Label(root, text="Angle 2")
angle3_label = ttk.Label(root, text="Angle 3")
angle4_label = ttk.Label(root, text="Angle 4")
pos1_label = ttk.Label(root, text="Position 1")
pos2_label = ttk.Label(root, text="Position 2")

arm_dis_entry = ttk.Entry(root, textvariable=arm_dis_var)
arm_len1_entry = ttk.Entry(root, textvariable=arm_len1_var)
arm_len2_entry = ttk.Entry(root, textvariable=arm_len2_var)
angle1_entry = ttk.Entry(root, textvariable=angle1_var)
angle2_entry = ttk.Entry(root, textvariable=angle2_var)
angle3_entry = ttk.Entry(root, textvariable=angle3_var)
angle4_entry = ttk.Entry(root, textvariable=angle4_var)
pos1_x_entry = ttk.Entry(root, textvariable=pos1_x_var)
pos1_y_entry = ttk.Entry(root, textvariable=pos1_y_var)
pos2_x_entry = ttk.Entry(root, textvariable=pos2_x_var)
pos2_y_entry = ttk.Entry(root, textvariable=pos2_y_var)

sub_btn = ttk.Button(root, text='Create Animation', command=draw_arms)
cal_btn = ttk.Button(root, text='Calculate Angle', command=calculate_angles)

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
angle3_label.grid(column=0, row=5)
angle3_entry.grid(column=1, row=5)
angle4_label.grid(column=0, row=6)
angle4_entry.grid(column=1, row=6)

pos1_label.grid(column=0, row=7)
pos1_x_entry.grid(column=1, row=7)
pos1_y_entry.grid(column=2, row=7)
pos2_label.grid(column=0, row=8)
pos2_x_entry.grid(column=1, row=8)
pos2_y_entry.grid(column=2, row=8)

cal_btn.grid(column=0, row=9, columnspan=3)
sub_btn.grid(column=0, row=10, columnspan=3)

canvas = tk.Canvas(root, bg="white", height=500, width=500)
canvas.create_line(0, 250, 500, 250, dash=(3, 1))
canvas.grid(column=0, row=11, columnspan=3)
root.mainloop()
