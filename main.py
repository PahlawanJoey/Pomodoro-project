from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    timer_text.config(text="Timer")
    checkmark_label.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    window.attributes('-topmost', 1)
    if reps % 8 == 0:
        timer_text.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_text.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_text.config(text="Work", fg=GREEN)
        count_down(work_sec)
    window.attributes('-topmost', 0)


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        checkmark_label.config(text=marks)


window = Tk()
window.title("PahlawanJoey's Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_text.grid(column=1, row=0)
start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)
reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
checkmark_label.grid(column=1, row=3)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background)
timer_count = canvas.create_text(100, 135, text="GOAT", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
