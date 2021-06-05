from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1

  work_secs = WORK_MIN * 60
  short_break_secs = SHORT_BREAK_MIN * 70
  long_break_secs = LONG_BREAK_MIN * 60

  if reps % 8 == 0:        
    count_down(long_break_secs)
    title.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    count_down(short_break_secs)
    title.config(text="Break", fg=PINK)
  else:
    count_down(work_secs)
    title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60

  if count_min < 10:
    count_min = f"0{count_min}"

  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    window.after(1000, count_down, count - 1)
  else:
    start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
title.grid(column=1, row=0)

checkmark = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=3)

button_start = Button(text="Start", command=start_timer, width=7, height=2, bg=GREEN, font=(FONT_NAME, 14, "bold"), highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", width=7, height=2, bg=GREEN, font=(FONT_NAME, 14, "bold"), highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()