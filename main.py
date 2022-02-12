from datetime import datetime
import time
from playsound import playsound
from tkinter import *


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 23:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"


class GUI:

    def __init__(self):
        window = Tk()
        window.title("Alarm Clock")
        window.geometry('400x400')
        self.lbl = Label(window, text="Enter time in 'HH:MM:SS' format: ")
        self.lbl.grid(column=0, row=0)
        self.alarm_time = Entry(window, width=20)
        self.alarm_time.grid(column=1, row=0)
        self.alarm_time.focus()
        btn = Button(window, text="Click Me", command=self.clicked)
        btn.grid(column=2, row=0)
        window.mainloop()

    def clicked(self):
        while True:
            alarm = self.alarm_time.get()
            validate = validate_time(alarm.lower())
            if validate != "ok":
                self.lbl.configure(text=validate)
            else:
                self.lbl.configure(text=f"Setting alarm for {alarm}...")
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
                        self.lbl.configure(text="Wake Up!")
                        # playsound('laugh.wav')
                        break


gui = GUI()

# underneath is code to run alarm in console

# while True:
#     alarm_time = input("Enter time in 'HH:MM:SS' format: ")
#
#     validate = validate_time(alarm_time.lower())
#     if validate != "ok":
#         print(validate)
#     else:
#         print(f"Setting alarm for {alarm_time}...")
#         break
# alarm_hour = alarm_time[0:2]
# alarm_min = alarm_time[3:5]
# alarm_sec = alarm_time[6:8]
#
# while True:
#     now = datetime.now()
#     current_hour = now.strftime("%H")
#     current_min = now.strftime("%M")
#     current_sec = now.strftime("%S")
#
#     if alarm_hour == current_hour:
#         if alarm_min == current_min:
#             if alarm_sec <= current_sec:
#                 print("Wake Up!")
#                 playsound('laugh.wav')
#                 break
