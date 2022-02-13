# the unblockme.py was implemented from https://github.com/KentZuntov/Unblock-Me
# the whackamole.py was implemented from https://github.com/sonlexqt/whack-a-mole

from datetime import datetime
import time
from tkinter import *
from threading import *
from random import randint
import simpleaudio as sa

import spaceinvaders
import unblockme
import whackamole


def validate_time(time_to_validate):
    if len(time_to_validate) != 8:
        return "Invalid time format! Please try again (HH:MM:SS)."
    else:
        if int(time_to_validate[0:2]) > 23:
            return "Invalid HOUR format! Please try again (HH:MM:SS)."
        elif int(time_to_validate[3:5]) > 59:
            return "Invalid MINUTE format! Please try again (HH:MM:SS)."
        elif int(time_to_validate[6:8]) > 59:
            return "Invalid SECOND format! Please try again (HH:MM:SS)."
        else:
            return "ok"


window = Tk()
window.title("Alarm Clock")
window.geometry('600x400')
lbl = Label(window, text="Enter time in 'HH:MM:SS' format: ")
lbl.grid(column=0, row=0)
alarm_time = Entry(window, width=20)
alarm_time.grid(column=1, row=0)
alarm_time.focus()

close_alarm = 1


def threading():
    t1 = Thread(target=clicked)
    t1.start()


def threading2():
    t2 = Thread(target=unblockme.playing)
    t2.start()
    btn2 = Button(window, text="Stop Alarm!", command=quitting)
    btn2.grid(column=2, row=0)


def threading3():
    t3 = Thread(target=whackamole.playing)
    t3.start()
    btn2 = Button(window, text="Stop Alarm!", command=quitting)
    btn2.grid(column=2, row=0)


def threading4():
    t3 = Thread(target=spaceinvaders.playing)
    t3.start()
    btn2 = Button(window, text="Stop Alarm!", command=quitting)
    btn2.grid(column=2, row=0)


def clicked():
    abc = None
    while True:
        if abc is not None:
            alarm = abc
        alarm = alarm_time.get()
        validate = validate_time(alarm.lower())
        if validate != "ok":
            abc = input(lbl.configure(text=validate))
        else:
            lbl.configure(text=f"Setting alarm for {alarm}...")
            alarm_time.grid_forget()
            btn.grid_forget()
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
                    value = randint(0, 1)
                    value = 2
                    lbl.configure(text="Wake Up!")
                    if value == 0:
                        btn2 = Button(window, text="Stop Alarm!", command=threading2)
                        btn2.grid(column=2, row=0)
                    elif value == 1:
                        btn2 = Button(window, text="Stop Alarm!", command=threading3)
                        btn2.grid(column=2, row=0)
                    elif value == 2:
                        btn2 = Button(window, text="Stop Alarm!", command=threading4)
                        btn2.grid(column=2, row=0)
                    while close_alarm:
                        wave_object = sa.WaveObject.from_wave_file('laugh.wav')
                        play_object = wave_object.play()
                        play_object.wait_done()
                    break


def quitting():
    global close_alarm
    sa.stop_all()
    close_alarm = 0
    lbl.configure(text=f"Alarm Stopped! Have a great day!")


btn = Button(window, text="Set Alarm", command=threading)
btn.grid(column=2, row=0)
window.mainloop()
