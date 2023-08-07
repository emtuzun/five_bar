import tkinter as tk
from tkinter import ttk
import math
import time

lines = []
move_trace = []
points = []
clicked = False
reversing = 0

# Click function


def click_fun(event):
    global clicked
    x = event.x - 250
    y = 250 - event.y
    try:
        a = float(arm_dis_var.get())/2
        arm_len = 2 * float(arm_len1_var.get()) + a
        if math.sqrt((x-a)**2+y**2) < arm_len and math.sqrt((x+a)**2+y**2) < arm_len:
            if not clicked:
                for i in range(len(points)):
                    canvas.delete(points[i])
                points.clear()
                pos1_x_var.set(str(x))
                pos1_y_var.set(str(y))
                points.append(canvas.create_oval(
                    event.x, event.y, event.x+2, event.y+2))
                canvas.update()
                clicked = True
            else:
                pos2_x_var.set(str(x))
                pos2_y_var.set(str(y))
                points.append(canvas.create_oval(
                    event.x, event.y, event.x+2, event.y+2))
                canvas.update()
                clicked = False
    except:
        print("hata")

# calculating angles


def calculate_angles():
    global reversing
    a = float(arm_dis_var.get())
    k = float(arm_len1_var.get())
    l = k+a/2
    x_1 = float(pos1_x_var.get())
    y_1 = float(pos1_y_var.get())
    x_2 = float(pos2_x_var.get())
    y_2 = float(pos2_y_var.get())
    reversing = y_1

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
    angle1_var.set(str(math.degrees(angle1)))
    angle2_var.set(str(math.degrees(angle2)))
    angle3_var.set(str(math.degrees(angle3)))
    angle4_var.set(str(math.degrees(angle4)))
    if reversing < 0:
        reversed = True
    else:
        reversed = False
    for i in range(len(move_trace)):
        canvas.delete(move_trace[i])
    move_trace.clear()
    draw_arms(a, k, angle1, angle2, reversed)

# creatin working plane


def create_working_plane():
    canvas.delete("all")
    try:
        x = float(arm_dis_var.get()) / 2
        arm_len1 = float(arm_len1_var.get())
        arm_len2 = arm_len1 + x
        z = arm_len1 + arm_len2
        y = math.sqrt(z**2 - x**2)
        alpha = math.acos((x**2 + z**2 - y**2)/(2*x*z))
        canvas.create_arc(250+x-z, 250-z, 250+x+z, 250+z, start=math.degrees(
            math.pi-alpha), extent=math.degrees(2*alpha), style=tk.ARC)
        canvas.create_arc(250-x-z, 250-z, 250-x+z, 250+z, start=math.degrees(
            2*math.pi-alpha), extent=math.degrees(2*alpha), style=tk.ARC)
        canvas.create_oval(250-x+arm_len1-arm_len2, 250+arm_len1-arm_len2, 250-x+arm_len2 -
                           arm_len1, 250+arm_len2-arm_len1)
        canvas.create_oval(250+x+arm_len1-arm_len2, 250+arm_len1-arm_len2, 250+x+arm_len2 -
                           arm_len1, 250+arm_len2-arm_len1)
        draw_arms(x*2, arm_len1, math.pi/2, math.pi/2, False)
    except:
        print("Degerler eksik girildi")

# drawing arms function


def draw_arms(arm_dis: float, arm_len1: float, angle1: float, angle2: float, reverse: bool):
    x_1 = 250-(arm_dis/2)+arm_len1*math.cos(angle1)
    y_1 = 250-arm_len1*math.sin(angle1)
    x_2 = 250+(arm_dis/2)+arm_len1*math.cos(angle2)
    y_2 = 250-arm_len1*math.sin(angle2)
    arm_len2 = arm_len1 + arm_dis/2
    d = math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2)
    h = math.sqrt(arm_len2**2 - (d/2)**2)
    if reverse:
        x_3 = ((x_1+x_2) / 2) - (h*(y_2-y_1))/d
        y_3 = ((y_1+y_2) / 2) + (h*(x_2-x_1))/d
    else:
        x_3 = ((x_1+x_2) / 2) + (h*(y_2-y_1))/d
        y_3 = ((y_1+y_2) / 2) - (h*(x_2-x_1))/d
    for i in range(len(lines)):
        canvas.delete(lines[i])
    lines.clear()
    lines.append(canvas.create_line(0, 250, 500, 250, dash=(3, 1)))
    lines.append(canvas.create_line(250-(arm_dis/2), 250, x_1, y_1))
    lines.append(canvas.create_line(x_1, y_1, x_3, y_3))
    lines.append(canvas.create_line(250+(arm_dis/2), 250, x_2, y_2))
    lines.append(canvas.create_line(x_2, y_2, x_3, y_3))
    move_trace.append(canvas.create_oval(x_3, y_3, x_3+1, y_3+1))

# move arms


def move_arms():
    for i in range(len(move_trace)):
        canvas.delete(move_trace[i])
    move_trace.clear()
    arm_dis = float(arm_dis_var.get())
    arm_len1 = float(arm_len1_var.get())
    angle1 = math.radians(float(angle1_var.get()))
    angle2 = math.radians(float(angle2_var.get()))
    angle3 = math.radians(float(angle3_var.get()))
    angle4 = math.radians(float(angle4_var.get()))
    # if angle1 > math.pi:
    #     angle1 -= 2 * math.pi
    # elif angle1 <-math.pi:
    #     angle1 += 2 * math.pi
    # if angle2 > math.pi:
    #     angle2 -= 2 * math.pi
    # elif angle2 <-math.pi:
    #     angle2 += 2 * math.pi
    # if angle3 > math.pi:
    #     angle3 -= 2 * math.pi
    # elif angle3 <-math.pi:
    #     angle3 += 2 * math.pi
    # if angle4 > math.pi:
    #     angle4 -= 2 * math.pi
    # elif angle4 <-math.pi:
    #     angle4 += 2 * math.pi
    n = 200
    if reversing < 0:
        reversed = True
    else:
        reversed = False
    for i in range(n):
        next_angle1 = angle1 + ((angle3-angle1)/n)*i
        next_angle2 = angle2 + ((angle4-angle2)/n)*i
        if next_angle1 == math.pi and next_angle2 == 0:
            reversed = not reversed
        draw_arms(arm_dis, arm_len1,
                  next_angle1, next_angle2, reversed)
        time.sleep(0.01)
        root.update()


# creating tk window
root = tk.Tk()
root.title("Five Bars")

arm_dis_var = tk.StringVar()
arm_len1_var = tk.StringVar()
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
angle1_label = ttk.Label(root, text="Angle 1")
angle2_label = ttk.Label(root, text="Angle 2")
angle3_label = ttk.Label(root, text="Angle 3")
angle4_label = ttk.Label(root, text="Angle 4")
pos1_label = ttk.Label(root, text="Position 1")
pos2_label = ttk.Label(root, text="Position 2")

arm_dis_entry = ttk.Entry(root, textvariable=arm_dis_var)
arm_len1_entry = ttk.Entry(root, textvariable=arm_len1_var)
angle1_entry = ttk.Entry(root, textvariable=angle1_var)
angle2_entry = ttk.Entry(root, textvariable=angle2_var)
angle3_entry = ttk.Entry(root, textvariable=angle3_var)
angle4_entry = ttk.Entry(root, textvariable=angle4_var)
pos1_x_entry = ttk.Entry(root, textvariable=pos1_x_var)
pos1_y_entry = ttk.Entry(root, textvariable=pos1_y_var)
pos2_x_entry = ttk.Entry(root, textvariable=pos2_x_var)
pos2_y_entry = ttk.Entry(root, textvariable=pos2_y_var)


sub_btn = ttk.Button(root, text='Create Animation', command=move_arms)
cal_btn = ttk.Button(root, text='Calculate Angle', command=calculate_angles)
create_plane_btn = ttk.Button(
    root, text='Create Working Plane', command=create_working_plane)

arm_dis_label.grid(column=0, row=0)
arm_dis_entry.grid(column=1, row=0)
arm_len1_label.grid(column=0, row=1)
arm_len1_entry.grid(column=1, row=1)
angle1_label.grid(column=0, row=2)
angle1_entry.grid(column=1, row=2)
angle2_label.grid(column=0, row=3)
angle2_entry.grid(column=1, row=3)
angle3_label.grid(column=0, row=4)
angle3_entry.grid(column=1, row=4)
angle4_label.grid(column=0, row=5)
angle4_entry.grid(column=1, row=5)

pos1_label.grid(column=0, row=6)
pos1_x_entry.grid(column=1, row=6)
pos1_y_entry.grid(column=2, row=6)
pos2_label.grid(column=0, row=7)
pos2_x_entry.grid(column=1, row=7)
pos2_y_entry.grid(column=2, row=7)

create_plane_btn.grid(column=0, row=8)
cal_btn.grid(column=1, row=8)
sub_btn.grid(column=2, row=8)

canvas = tk.Canvas(root, bg="white", height=500, width=500)
canvas.bind("<Button-1>", click_fun)
canvas.create_line(0, 250, 500, 250, dash=(3, 1))
canvas.grid(column=0, row=9, columnspan=3)
root.mainloop()
