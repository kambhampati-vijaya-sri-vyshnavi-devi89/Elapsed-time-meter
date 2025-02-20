import tkinter as Tkinter
from datetime import datetime

counter = 66600
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 66600:
                display = "Starting...⏳"
            else:
                tt = datetime.fromtimestamp(counter)
                display = tt.strftime("%H:%M:%S")
            label["text"] = display
            label.after(1000, count)
            counter += 1
    count()

def Start(label):
    global running
    running = True
    counter_label(label)
    start["state"] = "disabled"
    stop["state"] = "normal"
    reset["state"] = "normal"

def Stop():
    global running
    start["state"] = "normal"
    stop["state"] = "disabled"
    reset["state"] = "normal"
    running = False

def Reset(label):
    global counter
    counter = 66600
    label["text"] = "Click '▶' to Start⏱"

root = Tkinter.Tk()
root.title("Stopwatch")
root.configure(bg="yellow")

label = Tkinter.Label(root, text="Click '▶' to Start⏱", fg="#4B8BBE", bg="yellow", font="Verdana 25 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text="Start ▶", width=10, command=lambda: Start(label))
stop = Tkinter.Button(f, text="Pause ⏸", width=10, state="disabled", command=Stop)
reset = Tkinter.Button(f, text="Reset 🔁", width=10, state="disabled", command=lambda: Reset(label))
f.pack(anchor="center", pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")

root.mainloop()
