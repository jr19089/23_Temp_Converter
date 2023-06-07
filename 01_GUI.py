from tkinter import *
from random import shuffle

title = ["Temperature Converter", "I Can't Believe it's", "I'll do the converting, just put in the numbers",
         "Hi how are ya?", "Rigor Mormist", "What's the temperature?", "0 + 0 = 32 Degrees Fahrenheit",
         "It's Convertin Time", "And then he converted all over the place", "Smoke Bomb",
         "I just spent 6 months in a leaky boat *clap clap* *clap clap*",
         "Everybody Wang Chung tonight!",
         "Hello Traveller! A new quest has been added to the T-Bone Junction Bounty board!",
         "Hello, I am under the water", "It's Pizza Time!", ":)", "Good morning campers!", "CORROSION"]
shuffle(title)


class Converter:
    def __init__(self):
        self.temp_frame = Frame(padx=10, pady=10, bg='dark orange')
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Times", "20", "bold"),
                                  bg='dark orange')
        self.temp_heading.grid(row=0)

        instructions = "Select whether you want to convert to Celsius or Fahrenheit, " \
                       "then start converting!"
        self.temp_instructions = Label(self.temp_frame, text=instructions, bg='dark orange')
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Times", "20"))
        self.temp_entry.grid(row=2)

        error = "Please enter an actual number "
        self.temp_error = Label(self.temp_frame, text=error, bg='dark orange')
        self.temp_error.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.celsius_button = Button(self.button_frame,
                                     text="Celsius", bg='light sky blue', fg='navy', font=("arial", 14))
        self.celsius_button.grid(row=0, column=0, padx=15, pady=15)

        self.fahrenheit_button = Button(self.button_frame,
                                        text="Fahrenheit", bg='light sky blue', fg='navy', font=("arial", 14))
        self.fahrenheit_button.grid(row=0, column=1, padx=15, pady=15)

        self.help_button = Button(self.button_frame,
                                  text="Help!", bg='light sky blue', fg='navy', font=("arial", 14))
        self.help_button.grid(row=0, column=2, padx=16, pady=16)

        self.history_button = Button(self.button_frame,
                                     text="History", bg='light sky blue', fg='navy', font=("arial", 14),
                                     state=DISABLED)
        self.history_button.grid(row=0, column=3, padx=16, pady=16)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title(title[0])
    Converter()
    root.mainloop()
