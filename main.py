# the unblockme.py was implemented from https://github.com/KentZuntov/Unblock-Me
# the whackamole.py was implemented from https://github.com/sonlexqt/whack-a-mole
# the spaceinvaders.py was implemented from https://github.com/leerob/space-invaders
# the rpsgame.py was implemented from https://github.com/seekpl/rps-game
# the speedtyping.py was implemented from https://github.com/codecravings/Speed-Typing-Test-Python

# The main.py was written and implemented by Simon Bilodeau, Pate Lauzon, and Ryan Haniff for the Polyhacks 2022
# event. This program is an alarm clock that will not stop until a game is won. The game that needs to be played
# is chosen at random within the games that have been implemented from seperate .py files. The goal of this program
# is for the user to be forced to use their brain to close their alarm, forcing the brain to stay awake once the
# game has been played.

# Feel free to use this code in any other project.

from datetime import datetime
import time
from tkinter import *
from threading import *
from random import randint
import simpleaudio as sa

import rpsgame
import spaceinvaders
import speedtyping
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


def threading5():
    t5 = Thread(target=rpsgame.playing)
    t5.start()
    btn2 = Button(window, text="Stop Alarm!", command=quitting)
    btn2.grid(column=2, row=0)


def threading6():
    t6 = Thread(target=speedtyping.playing)
    t6.start()
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
                    value = randint(0, 4)
                    print(value)
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
                    elif value == 3:
                        btn2 = Button(window, text="Stop Alarm!", command=threading5)
                        btn2.grid(column=2, row=0)
                    elif value == 4:
                        btn2 = Button(window, text="Stop Alarm!", command=threading6)
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
