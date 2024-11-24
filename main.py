import tkinter as tk
import random

root = tk.Tk()
root.title("Animation Drawing Screen")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.pack()

balls = []

ball_colors = ["red", "blue", "green", "yellow", "gray"]

continue_animation = False

size_label = tk.Label(root, text="Select Size:")
size_label.pack()
size_var = tk.IntVar(value=20)
size_menu = tk.OptionMenu(root, size_var, 20, 30, 50)
size_menu.pack()

color_label = tk.Label(root, text="Select Color:")
color_label.pack()
color_var = tk.StringVar(value=ball_colors[0])
color_menu = tk.OptionMenu(root, color_var, *ball_colors)
color_menu.pack()

def add_ball():
    size = size_var.get()
    color = color_var.get()
    x = random.randint(size, 800 - size)
    y = random.randint(size, 500 - size)
    ball = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
    balls.append({"id": ball, "dx": random.choice([-3, 3]), "dy": random.choice([-3, 3])})

def move_balls():
    global continue_animation
    if not continue_animation:
        return
    for ball in balls:
        x1, y1, x2, y2 = canvas.coords(ball["id"])
        if x1 <= 0 or x2 >= 800:
            ball["dx"] = -ball["dx"]
        if y1 <= 0 or y2 >= 500:
            ball["dy"] = -ball["dy"]
        canvas.move(ball["id"], ball["dx"], ball["dy"])
    root.after(30, move_balls)

def start():
    global continue_animation
    continue_animation = True
    move_balls()

def stop():
    global continue_animation
    continue_animation = False

def reset():
    global balls
    for ball in balls:
        canvas.delete(ball["id"])
    balls = []

def speed_up():
    for ball in balls:
        ball["dx"] *= 1.5
        ball["dy"] *= 1.5

frame = tk.Frame(root)
frame.pack()

add_button = tk.Button(frame, text="Add Ball", command=add_ball)
add_button.pack(side=tk.LEFT)

start_button = tk.Button(frame, text="Start", command=start)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(frame, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT)

reset_button = tk.Button(frame, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT)

speed_button = tk.Button(frame, text="Speed Up", command=speed_up)
speed_button.pack(side=tk.LEFT)

root.mainloop()
