import time
import tkinter
from tkinter import *
import random
from threading import *


class TextFlash:
    def __init__(self):
        self.random_word = ""
        self.hackatown_word_list = []
        self.rand = 0
        # self.label_countdown
        # self.lbl_rules
        # self.lbl_question

    hackatown_word_list = ["polyhacks", "hackatown", "raffle guy", "ovhcloud"]

    window = Tk()
    window.title("Text Flash Game")
    window.geometry("700x450")
    window.configure(bg="orange red")

    # center this label
    lbl_rules = Label(window, text="Text will be flash one the screen,\n type it in to disable the alarm",
                      bg="orange red",
                      fg="white", font="none 24 bold")
    lbl_rules.config(anchor=CENTER)
    lbl_rules.pack()

    # lbl2 = Label(window, text="Enter something here:", bg="orange red", fg="white", font="none 12 bold")
    # lbl2.config()
    # lbl2.pack()

    # def threading(self):
    #     t1 = Thread(target=timer)
    #     t1.start()

    random_word = ""
    rand = random.randint(0, len(hackatown_word_list) - 1)
    print(hackatown_word_list[rand])

    def random_word_update(self):
        global rand
        rand = random.randint(0, len(self.hackatown_word_list) - 1)

    initial_time = 10
    int_count_down = initial_time

    def update_flash(self):
        global lbl_flash
        self.random_word_update()
        lbl_flash = Label(self.window, text=self.hackatown_word_list[rand], bg="black", fg="white", font="none 16 bold")
        lbl_flash.place(x=random.randint(0, 600), y=random.randint(0, 350))
        self.window.after(1000, lbl_flash.destroy)

    def timer(self):
        global int_count_down
        int_count_down -= 1
        self.label_countdown.config(text=int_count_down)
        if int_count_down <= 1:
            self.update_flash()
            int_count_down = self.initial_time
        self.label_countdown.after(1000, self.timer)

    def on_enter(self, e):
        global enter_window
        string_val = enter_window.get()
        print(string_val)
        if string_val == self.hackatown_word_list[rand]:
            self.lbl_question.config(text="Correct")
            print("correct")
            self.lbl_question.update()
            self.label_countdown.destroy()

    update_flash()
    # lbl_flash = Label(window, text=hackatown_word_list[rand], bg="red", fg="white", font="none 12 bold")
    # lbl_flash.place(x=random.randint(0, 600), y=random.randint(0, 350))

    lbl_question = Label(window, text="What was the word?", bg="orange red", fg="white", font="none 12 bold")
    lbl_question.place(relx=0.5, rely=0.85, anchor='s')

    # window.after(1000, lbl_flash.destroy)

    enter_window = Entry(window, bg="white", fg="black", font="none 12 bold")
    enter_window.place(relx=0.5, rely=0.9, anchor='s')

    label_countdown = Label(window, text="test", bg="orange red", fg="white", font="none 18 bold")
    label_countdown.place(relx=0.5, rely=0.5, anchor='center')
    timer()

    enter_window.bind("<Return>", on_enter)

    window.mainloop()

