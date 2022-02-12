import threading
from asyncio import sleep
from random import random
from tkinter import *


def playing():
    whacks = 0
    hole = 0

    def leftClick(event):
        global whacks
        whacks = 0
        frame.config(bg='red')
        scorelabel.config(text="* " + str(whacks) + " *")

    screen = Tk()
    frame = Frame(screen, bg='green', width=500, height=520)
    frame.bind("<Button-1>", leftClick)
    frame.pack()
    # screen.config(bg="green", width=500, height=520)
    screen.resizable(0, 0)
    # screen.attributes('-topmost', True)
    lab = Label(text="WHAC-A-MOLE!", font=("Arial", 30), bg='blue', fg='yellow')
    lab.place(x=110, y=0)
    scorelabel = Label(text=whacks, width=7, font=('Arial', 30), bg='yellow')
    scorelabel.place(x=170, y=52)

    def onwhack():
        global hole
        global whacks
        if hole == 1:
            hole1.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 2:
            hole2.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 3:
            hole3.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 4:
            hole4.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 5:
            hole5.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 6:
            hole6.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 7:
            hole7.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 8:
            hole8.config(state='normal', text='*_*', bg='red', fg='black')
        elif hole == 9:
            hole9.config(state='normal', text='*_*', bg='red', fg='black')
        else:
            whacks = 0
        whacks += 1
        if whacks == 10:
            sys.exit()
        scorelabel.config(text="* " + str(whacks) + " *")

    hole1 = Button(
        width=3,
        height=5,
        bg='black',
        state='disabled',
        command=onwhack)
    hole1.place(x=3, y=135)
    hole2 = Button(
        width=2,
        height=6,
        bg='black',
        state='disabled',
        command=onwhack)
    hole2.place(x=75, y=220)
    hole3 = Button(
        width=10,
        height=2,
        bg='black',
        state='disabled',
        command=onwhack)
    hole3.place(x=22, y=395)
    hole4 = Button(
        width=24,
        height=1,
        bg='black',
        state='disabled',
        command=onwhack)
    hole4.place(x=150, y=115)
    hole5 = Button(
        width=8,
        height=4,
        bg='black',
        state='disabled',
        command=onwhack)
    hole5.place(x=170, y=265)
    hole6 = Button(
        width=10,
        height=2,
        bg='black',
        state='disabled',
        command=onwhack)
    hole6.place(x=170, y=450)
    hole7 = Button(
        width=4,
        height=4,
        bg='black',
        state='disabled',
        command=onwhack)
    hole7.place(x=370, y=155)
    hole8 = Button(
        width=1,
        height=2,
        bg='black',
        state='disabled',
        command=onwhack)
    hole8.place(x=320, y=285)
    hole9 = Button(
        width=6,
        height=3,
        bg='black',
        state='disabled',
        command=onwhack)
    hole9.place(x=343, y=395)

    def start():
        global whacks
        whacks = 0
        t = threading.Thread(target=whac_a_mole)
        t.start()

    # make text bold
    def whac_a_mole():
        ready_set_whack()
        global hole
        while True:
            hole = random.randint(1, 9)
            frame.config(bg='green')
            if hole == 1:
                hole1.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole1.config(state='disabled', text='', bg='black')
            elif hole == 2:
                hole2.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole2.config(state='disabled', text='', bg='black')
            elif hole == 3:
                hole3.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole3.config(state='disabled', text='', bg='black')
            elif hole == 4:
                hole4.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole4.config(state='disabled', text='', bg='black')
            elif hole == 5:
                hole5.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole5.config(state='disabled', text='', bg='black')
            elif hole == 6:
                hole6.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole6.config(state='disabled', text='', bg='black')
            elif hole == 7:
                hole7.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole7.config(state='disabled', text='', bg='black')
            elif hole == 8:
                hole8.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole8.config(state='disabled', text='', bg='black')
            elif hole == 9:
                hole9.config(
                    state='normal',
                    text='X',
                    bg='pink',
                    fg='black')
                sleep(0.8)
                hole9.config(state='disabled', text='', bg='black')

    def ready_set_whack():
        sleep(1)
        scorelabel.config(text="Ready")
        sleep(1)
        scorelabel.config(text="Set")
        sleep(1)
        scorelabel.config(text="WHACK!")
        sleep(1)
        scorelabel.config(text="0")

    start()

    screen.mainloop()
