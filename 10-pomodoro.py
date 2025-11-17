from tkinter import *
import math

#  Constants
RED = "#BF1A1A"
PINK = "#FF8FB7"
GREEN = "#3A6F43"
SHORT_BREAK_SECS = 300
LONG_BREAK_SECS = 1200
WORK_SECS = 1500
reps = 0 
timer = None

# Function reset_timer 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer", fg = "#9bdeac")
    check_mark.config(text = "")
    global reps
    reps = 0

# Function start_timer
def start_timer():
    global reps
    reps +=1
    if reps % 2 == 1:
        count_down(WORK_SECS)
        title_label.config(text = "Work", fg = GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SECS)
        title_label.config(text = "Break", fg = RED)
    elif reps == 8:
        count_down(LONG_BREAK_SECS)
        title_label.config(text = "Break", fg = PINK)
    

# Function countdown 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text = f"{count_minutes:02d}:{count_seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)    
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text = marks)

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="#FFF8D4")

title_label = Label(text = "Timer", fg = "#9bdeac", bg = "#FFF8D4", font = ("Courier", 50, "bold"))
title_label.grid(column = 1, row = 0)

canvas = Canvas(width=220, height=224, bg="#FFF8D4", highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(103, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill = "white", font=("courier", 35, "bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", highlightthickness = 0, command = reset_timer)
reset_button.grid(column = 2, row = 2)

#check_mark = Label(text = "✓", fg = "#9bdeac", bg = "#FFF8D4")
check_mark = Label(text = "", fg = "#9bdeac", bg = "#FFF8D4")
check_mark.grid(column = 1, row = 3)

window.mainloop()