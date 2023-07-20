from tkinter import *
from random import shuffle

title = ["Temperature Converter", "I Can't Believe it's", "I'll do the converting, just put in the numbers",
         "Hi how are ya?", "Rigor Mormist", "What's the temperature?", "0 + 0 = 32 Degrees Fahrenheit",
         "It's Convertin Time", "And then he converted all over the place", "Smoke Bomb",
         "I just spent 6 months in a leaky boat *clap clap* *clap clap*",
         "Everybody Wang Chung tonight!",
         "Hello Traveller! A new quest has been added to the T-Bone Junction Bounty board!",
         "Hello, I am under the water", "It's Pizza Time!", ":)", "Good morning campers!", "CORROSION",
         "Michael! Don't leave me here! MICHAEL!", "The Fog Is Coming", "Hee to the Ho", "na na na na na na",
         "Too much time has been spent writing these", "*Didgeridoo plays aggressively*", "The Baby",
         "Turn on the AC already", "Porygon used Conversion", "My friends are my power!", "This sentence has 4 words"]
shuffle(title)


class Converter:
    def __init__(self):

        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_feedback.set("no")

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

        self.temp_error = Label(self.temp_frame, text="", bg='dark orange')
        self.temp_error.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.celsius_button = Button(self.button_frame,
                                     text="Celsius", bg='light sky blue', fg='navy', font=("arial", 14),
                                     command=lambda: self.temp_converter(-459))
        self.celsius_button.grid(row=0, column=0, padx=15, pady=15)

        self.fahrenheit_button = Button(self.button_frame,
                                        text="Fahrenheit", bg='light sky blue', fg='navy', font=("arial", 14),
                                        command=lambda: self.temp_converter(-273))
        self.fahrenheit_button.grid(row=0, column=1, padx=15, pady=15)

        self.help_button = Button(self.button_frame,
                                  text="Help!", bg='light sky blue', fg='navy', font=("arial", 14))
        self.help_button.grid(row=0, column=2, padx=16, pady=16)

        self.history_button = Button(self.button_frame,
                                     text="History", bg='light sky blue', fg='navy', font=("arial", 14),
                                     state=DISABLED)
        self.history_button.grid(row=0, column=3, padx=16, pady=16)

    def check_temp(self, min_value):
        error = "Please enter a valid temperature"
        try:
            response = self.temp_entry.get()
            response = float(response)
            if response < min_value:
                self.var_has_error.set("yes")
                self.temp_error.config(text=error)
            elif response == "":
                self.var_has_error.set("yes")
                self.temp_error.config(text=error)
            else:
                self.var_has_error.set("no")
                self.temp_error.config(text="")
                return response

        except ValueError:
            self.var_has_error.set("yes")
            self.temp_error.config(text=error)

    def temp_converter(self, min_val):
        to_convert = self.check_temp(min_val)
        deg_sign = u'\N{DEGREE SIGN}'
        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert != "invalid":
            set_feedback = "no"

        elif min_val == -459:
            answer = (to_convert - 32) * 5/9
            from_to = "{} F{} is {} C{}"
        else:
            answer = to_convert * 1.8 + 32
            from_to = "{} F{} is {} C{}"

        if set_feedback == "yes":
            feedback = from_to.format(to_convert, deg_sign, answer, deg_sign)
            self.var_feedback.set(feedback)

        self.output_answer()

    def output_answer(self):
        self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            self.temp_entry.config(bg='light pink')
            self.temp_entry.config(fg='red')
            self.temp_error.config(fg='red')
        else:
            self.temp_entry.config(bg='white')
            self.temp_entry.config(fg='black')


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title(title[0])
    Converter()
    root.mainloop()
