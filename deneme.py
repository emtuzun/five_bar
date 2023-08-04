import tkinter as tk
import time

# initial x position of the ball
animation_ball_start_xpos = 50
# initial y position of the ball
animation_ball_start_ypos = 50
# radius of the ball
animation_ball_radius = 30
# the pixel movement of ball for each iteration
animation_ball_min_movement = 5


# Create and animate ball in an infinite loop


def animate_ball(window, canvas, xinc, yinc):
    ball = canvas.create_oval(animation_ball_start_xpos-animation_ball_radius,
                              animation_ball_start_ypos-animation_ball_radius,
                              animation_ball_start_xpos+animation_ball_radius,
                              animation_ball_start_ypos+animation_ball_radius,
                              fill="blue", outline="white", width=4)
    while True:
        canvas.move(ball, xinc, yinc)
        window.update()
        time.sleep(0.01)
        ball_pos = canvas.coords(ball)
        # unpack array to variables
        xl, yl, xr, yr = ball_pos
        if xl < abs(xinc) or xr > 800-abs(xinc):
            xinc = -xinc
        if yl < abs(yinc) or yr > 600-abs(yinc):
            yinc = -yinc


# tkinter
root = tk.Tk()
root.title("Tkinter Animation Demo")
root.geometry('800x600')

# canvas
animation_canvas = tk.Canvas(root)
animation_canvas.configure(bg="black")
animation_canvas.pack(fill="both", expand=True)


animate_ball(root, animation_canvas,
             animation_ball_min_movement, animation_ball_min_movement)
