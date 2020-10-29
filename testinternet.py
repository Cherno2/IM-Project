#!/usr/bin/env python3
import tkinter as tk
import random
from functools import partial

guessnumber = random.randint(1,100)
tries = 0

def input_evaluate(inputfield, output_label, tries_label):
    
    global tries

    try:
        entery = int(inputfield.get())
    except ValueError:
        reply = "We search a number!"
    else:
        if entery == 0:
            reply = "Ohno, don´t we search a number from 1-100?"
        elif entery < 0:
            reply = "We search a positive number!"
        elif entery > 100:
            reply = ("Way too big maximum 100")
        elif entery == guessnumber:
            reply = "Congratulations you have guessed the right number!"
        elif entery < guessnumber:
            reply = ("Sorry, too small")
        elif entery > guessnumber:
            reply = "Sorry, too big"
        else:
            assert False
    tries +=1
    tries_label["text"] = tries
    output_label["text"] = reply
    

def main():
    
    title = "Guess Number Game"

    window = tk.Tk()
    window.title(title)
    window["background"] = "#E0EEE0"

    tk.Label(
        window,
        text=title,
        bg="turquoise",
        fg="red",
        font=("Helvetica Neue", 20),
    ).grid(row = 0, column =0 )

    number_label = tk.Label(
        window,
        text="Input number between 1-100:"
    )
    number_label.grid(row=1, column=0)

    output_label = tk.Label(
        window,
        text="Let´s beginn :)!",
        bg="blue",
        fg="white",
        font=("Arial", 15),
    )
    output_label.grid(row = 1, column =3)
   
    text = "Number between 1 - 100"
    inputfeld = tk.Entry(window, width=len(text), text=text)
    inputfeld.grid(row = 1, column = 1)

    triestext_label = tk.Label(
        window,
        text="How many tries:",
    )
    triestext_label.grid(row = 2, column = 0 )

    tries_label = tk.Label(
        window,
        text= "0",
    )
    tries_label.grid(row=2,column=2)
    

    tk.Button(
        window,
        text="Submit trail!",
        font=("Arial", 10),
        bg="orange",
        command=partial(input_evaluate, inputfeld, output_label, tries_label),
    ).grid(row = 3, column = 0)

    exit_button= tk.Button(window, text="Close Game", command=window.quit)
    exit_button.grid(row=3, column=2)

    window.mainloop()


if __name__ == "__main__":
    main()