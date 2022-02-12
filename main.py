from datetime import datetime
import time
# from playsound import playsound
from tkinter import *
from threading import *


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Invalid time format! Please try again (HH:MM:SS)."
    else:
        if int(alarm_time[0:2]) > 23:
            return "Invalid HOUR format! Please try again (HH:MM:SS)."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again (HH:MM:SS)."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again (HH:MM:SS)."
        else:
            return "ok"


window = Tk()
window.title("Alarm Clock")
window.geometry('400x400')
lbl = Label(window, text="Enter time in 'HH:MM:SS' format: ")
lbl.grid(column=0, row=0)
alarm_time = Entry(window, width=20)
alarm_time.grid(column=1, row=0)
alarm_time.focus()


def threading():
    t1 = Thread(target=clicked)
    t1.start()


def clicked():
    while True:
        alarm = alarm_time.get()
        validate = validate_time(alarm.lower())
        if validate != "ok":
            lbl.configure(text=validate)
        else:
            lbl.configure(text=f"Setting alarm for {alarm}...")
            break
    alarm_hour = alarm[0:2]
    alarm_min = alarm[3:5]
    alarm_sec = alarm[6:8]

    while True:
        time.sleep(1)
        now = datetime.now()
        current_hour = now.strftime("%H")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")

        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec <= current_sec:
                    lbl.configure(text="Wake Up!")
                    # playsound('laugh.wav')
                    break


btn = Button(window, text="Click Me", command=threading)
btn.grid(column=2, row=0)
window.mainloop()
