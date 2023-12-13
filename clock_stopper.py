from tkinter import *
import time

window = Tk()
window.title("STOP-IT")
window.geometry("600x400+400+10")
window.resizable(False, False)

time_data = StringVar()
start_time = 0 #this is no need
running = False

def start():
    global start_time, running
    start_time = time.time()
    running = True
    update_time()

def stop():
    global running
    if running == False:
        pass
    else: 
        running = False
        score()

def score():
    if time_data.get() == (f'00:10.000'):
        result="YOU WON"
    else:
        result="YOU LOOSE"

    score_window=Tk()
    score_window.title("SCORE BOARD")
    score_window.geometry("600x400+400+10")
    display = Label(score_window, text=result, width=60, height=13, bg="black", fg="green",font=("Arial",50))
    display.pack()
    score_window.mainloop()

def update_time():
    global running, start_time
    if running:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 1000) % 1000)
        time_data.set(f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}")
        window.after(10, update_time)

display = Label(window, textvariable=time_data, width=60, height=13, bg="black", fg="green",font=("Arial",50))
display.pack()


stop_button = Button(window, text="Stop", fg="green", bg="black", width=5, font=("Arial", 20),
                     activebackground="black", activeforeground="green", relief=SUNKEN, bd=4, command=stop)
stop_button.place(x=240, y=250)

start_button = Button(window, text="Start", fg="green", bg="black", width=5, font=("Arial", 20),
                      activebackground="black", activeforeground="green", relief=SUNKEN, bd=4, command=start)
start_button.place(x=240, y=330)

window.mainloop()
