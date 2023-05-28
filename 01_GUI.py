from tkinter import *
from random import shuffle

title = ["Temperature Converter", "I Can't Believe it's", "I'll do the converting, just put in the numbers",
         "Hi how are ya?", "Rigor Mormist", "What's the temperature?", "0 + 0 = 32 Degrees Fahrenheit",
         "It's Convertin Time", "And then he converted all over the place", "Smoke Bomb",
         "I just spent 6 months in a leaky boat *clap clap* *clap clap*",
         "Everybody Wang Chung tonight!", "Hello Traveller! A new quest has been added to the T-Bone Junction Bounty board!",
         "Hello! I am under the water!", "It's Pizza Time!", ":)"]
shuffle(title)


class Converter:
    def __init__(self):
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Times", "17", "bold"))

        self.temp_heading.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title(title[0])
    Converter()
    root.mainloop()
