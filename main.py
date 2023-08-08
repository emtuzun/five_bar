import tkinter as tk
from tkinter import ttk
import math
import time

lines = []
move_trace = []
points = []
clicked = False

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


# calculating angle for a point

def angle_of_point(x, y):
    a = float(arm_dis_var.get())
    k = float(arm_len1_var.get())
    l = k+a/2

    b = math.sqrt(y**2 + (x-a/2)**2)
    c = math.sqrt(y**2 + (x+a/2)**2)
    alpha_1 = math.acos((a**2 + b**2 - c**2)/(2*a*b))
    alpha_2 = math.acos((k**2 + b**2 - l**2)/(2*k*b))
    beta_1 = math.acos((a**2 + c**2 - b**2)/(2*a*c))
    beta_2 = math.acos((k**2 + c**2 - l**2)/(2*k*c))
    angle1 = beta_1+beta_2
    angle2 = math.pi - (alpha_1 + alpha_2)
    if (y < 0):
        angle1 = -angle1
        angle2 = -angle2
    return angle1, angle2

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
    pos1_x = float(pos1_x_var.get())
    pos1_y = float(pos1_y_var.get())
    pos2_x = float(pos2_x_var.get())
    pos2_y = float(pos2_y_var.get())
    if pos1_y < 0:
        reversed = True
    else:
        reversed = False

    if (pos2_x - pos1_x == 0):
        m = math.inf
    else:
        m = (pos2_y - pos1_y)/(pos2_x - pos1_x)
    n = pos1_y - m*pos1_x
    k = 200
    point_y = pos1_y
    for i in range(k+1):
        point_x = pos1_x + i*((pos2_x-pos1_x)/k)
        old_y = point_y
        if m == math.inf:
            point_y = pos1_y + i*((pos2_y-pos1_y)/k)
        else:
            point_y = m*(pos1_x + i*((pos2_x - pos1_x)/k))+n
        angle1, angle2 = angle_of_point(point_x, point_y)
        if (point_y <= 0 and old_y > 0) or (point_y >= 0 and old_y < 0):
            reversed = not reversed
        draw_arms(arm_dis, arm_len1, angle1, angle2, reversed)
        time.sleep(0.01)
        root.update()


# creating tk window
root = tk.Tk()
root.title("Five Bars")

arm_dis_var = tk.StringVar()
arm_len1_var = tk.StringVar()
pos1_x_var = tk.StringVar()
pos1_y_var = tk.StringVar()
pos2_x_var = tk.StringVar()
pos2_y_var = tk.StringVar()

arm_dis_label = ttk.Label(root, text="Arm Distance")
arm_len1_label = ttk.Label(root, text="Arm Length 1")
pos1_label = ttk.Label(root, text="Position 1")
pos2_label = ttk.Label(root, text="Position 2")

arm_dis_entry = ttk.Entry(root, textvariable=arm_dis_var)
arm_len1_entry = ttk.Entry(root, textvariable=arm_len1_var)
pos1_x_entry = ttk.Entry(root, textvariable=pos1_x_var)
pos1_y_entry = ttk.Entry(root, textvariable=pos1_y_var)
pos2_x_entry = ttk.Entry(root, textvariable=pos2_x_var)
pos2_y_entry = ttk.Entry(root, textvariable=pos2_y_var)


sub_btn = ttk.Button(root, text='Create Animation', command=move_arms)
create_plane_btn = ttk.Button(
    root, text='Create Working Plane', command=create_working_plane)

arm_dis_label.grid(column=0, row=0)
arm_dis_entry.grid(column=1, row=0)
arm_len1_label.grid(column=0, row=1)
arm_len1_entry.grid(column=1, row=1)

pos1_label.grid(column=0, row=3)
pos1_x_entry.grid(column=1, row=3)
pos1_y_entry.grid(column=2, row=3)
pos2_label.grid(column=0, row=4)
pos2_x_entry.grid(column=1, row=4)
pos2_y_entry.grid(column=2, row=4)

create_plane_btn.grid(column=0, row=5)
sub_btn.grid(column=2, row=5)

canvas = tk.Canvas(root, bg="white", height=500, width=500)
canvas.bind("<Button-1>", click_fun)
canvas.create_line(0, 250, 500, 250, dash=(3, 1))
canvas.grid(column=0, row=6, columnspan=3)
root.mainloop()
